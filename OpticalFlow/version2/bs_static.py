import sys
import numpy as np 
import cv2

# video file open
cap = cv2.VideoCapture('/mnt/35e7fe82-1988-46bd-a8c4-c1653d4b2a56/datascenter/Drone_flight_telemetry/fin.mp4')

if not cap.isOpened():
    print('video open failed')
    sys.exit()

# Enrool background
ret, back = cap.read() 
if not ret:
    print('Background image registration failed!')
    sys.exit()

back = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
back = cv2.GaussianBlur(back, (0,0), 1.0)

# Video process
while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (0,0), 1.0)

    # substack
    sub = cv2.absdiff(gray, back)
    _, sub = cv2.threshold(sub, 30, 255, cv2.THRESH_BINARY)

    #boxing
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(sub)

    for i in range(1, cnt):
        x, y, w, h, s = stats[i]

        if s < 75:
            continue

        cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 1)


    cv2.imshow('frame', frame)
    cv2.imshow('subtrack', sub)

    if cv2.waitKey(30) == 27:
        break
cap.release()
cv2.destroyAllWindows()