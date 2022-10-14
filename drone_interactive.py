import pygame
import cv2
from djitellopy import Tello
import time

# initializing pygame, setting title and connecting to our drone
pygame.init()
drone = Tello()
drone.connect(False)
# drone.streamon()
pygame.display.set_caption("Drone Control")

# Drawing a screen
window = pygame.display.set_mode((650, 500))
# Loading our background image for the controls
background = pygame.image.load('assets/tello_bg.png')

# This function will return True or False
# IF the specified key is pressed by the User


def get_key_press(key_name: str):
    is_pressed = False
    list_keys = pygame.key.get_pressed()
    my_key = getattr(pygame, f'K_{key_name}')
    if list_keys[my_key]:
        is_pressed = True
    pygame.display.update()

    return is_pressed


while True:
    window.fill((255, 255, 255))
    # bg image is off by 1 pixel...
    window.blit(background, (-1, 0))

    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 100

    if get_key_press("LEFT"):
        lr = -speed
    elif get_key_press("RIGHT"):
        lr = speed

    if get_key_press("UP"):
        fb = speed
    elif get_key_press("DOWN"):
        fb = -speed

    if get_key_press("w"):
        ud = speed
    elif get_key_press("s"):
        ud = -speed

    if get_key_press("a"):
        yv = -speed
    elif get_key_press("d"):
        yv = speed

    if get_key_press("e"):
        drone.land()

    if get_key_press("t"):
        drone.takeoff()

    if get_key_press("z"):
        cv2.imwrite(f'Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    if get_key_press("q"):
        print('Exiting')
        break

    img = drone.get_frame_read().frame
    img = cv2.resize(img, (300, 200))
    cv2.imshow("Display", img)
    drone.send_rc_control(lr, fb, ud, yv)

    cv2.waitKey(1)
    pygame.display.flip()
