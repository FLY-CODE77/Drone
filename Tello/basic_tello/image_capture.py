from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())
# me.stramon

me.streamon()

'''
Set video stream on.
If the response is 'Unknown command' means you have to update the Tello firmware. That
can be done through the Tello app.
Returns
bool: True for successful, False for unsuccessful
'''
while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow('img', img)
    cv2.waitKey(1)