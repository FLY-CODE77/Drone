from time import sleep
from djitellopy import tello
import keyboard as kp

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
    lr, fb, ud, yaw = 0, 0, 0, 0 
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yaw = -speed
    elif kp.getKey("d"): yaw = +speed

    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()

    return [lr, fb, ud, yaw]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.5)
    

 

import pygame

def init():

    pygame.init()

    win = pygame.display.set_mode((400, 400))

def getKey(keyName):

    ans = False

    for eve in pygame.event.get(): pass

    keyInput = pygame.key.get_pressed()

    myKey = getattr(pygame, "K_{}".format(keyName))

    print("K_{}".format(keyName))

    if keyInput[myKey]:

        ans = True

    pygame.display.update()

    return ans

def main():

    if getKey("LEFT"):

        print("Left key pressed")

    if getKey("RIGHT"):

        print("Right key Pressed")

if __name__ == "__main__":

    init()

    while True:

        main()