from djitellopy import tello
import cv2 

me = tello.Tello()
me.connect()

me.streamon()

while True:
    img = me.get_frame_read().frame # image receive
    img = cv2.resize(img, (360, 240))
    cv2.imshow("img", img)
    cv2.waitKey(1)
    
