# tello module import 
from djitellopy import tello
from time import sleep

# connect to Tello
me = tello.Tello()
me.connect()8

# show how much battery remain
print(me.get_battery())

# takeoff command
me.takeoff()

# rc control command 
'''Send RC control via four channels.
Arguments:
left_right_velocity: -100~100 (left/right)
forward_backward_velocity: -100~100 (forward/backward)
up_down_velocity: -100~100 (up/down)
yaw_velocity: -100~100 (yaw)
Returns:
bool: True for successful, False for unsuccessful
'''
# move forward 
me.send_rc_control(0, 50, 0, 0)
sleep(2)
# move yaw 
me.send_rc_control(0, 0, 0, 30)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
me.land()