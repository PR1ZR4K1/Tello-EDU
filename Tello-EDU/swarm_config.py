from djitellopy import Tello
from time import sleep
drone = Tello()

drone.connect()
# drone.set_wifi_credentials("Group_5", "12345678")

print(f'Battery: {drone.get_battery()}%')

# drone.connect_to_wifi("TP-Link_A66E", "80742982")
