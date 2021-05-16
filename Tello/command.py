# !pip install djitellopy
from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())


# takeoff
# control
me.takeoff()
sleep(2)

me.send_rc_control(0, 20, 0, 0) # left right , forward, up and down, yaw val
sleep(2) # 2second go

me.send_rc_control(10, 0, 0, 0) # left right , forward, up and down, yaw val
sleep(2) # 2second go

me.send_rc_control(0, 0, 0, 30) # left right , forward, up and down, yaw val
sleep(2) # 2second go

me.send_rc_control(0, 0, 0, 0) # stop and go 

me.land()



