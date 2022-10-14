from djitellopy import Tello
from time import sleep
drone = Tello()

drone.connect()
# set ssid name and password for individual tello

drone.set_wifi_credentials("Group_5", "12345678")

# connects drone to router

drone.connect_to_wifi("TP-Link-Router", "80742982")

