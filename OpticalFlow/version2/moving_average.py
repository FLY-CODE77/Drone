import cv2
import sys
import numpy as np 

cap = cv2.VideoCapture('/mnt/35e7fe82-1988-46bd-a8c4-c1653d4b2a56/datascenter/Drone_flight_telemetry/fin.mp4')

if not cap.isOpened():
    print("video load fail")
    sys.exit()

ret, back = cap.read()

if not ret:
    print("background image registration fail")
    sys.exit()

# back : uint8, fback: float32
back = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
back = cv2.GaussianBlur(back, (0,0), 1.0)
fback = back.astype(np.float32)

# Video process
while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (0,0), 0.95)

    # back : uint8, fback : float32
    cv2.accumulateWeighted(gray, fback, 0.025)
    back = fback.astype(np.uint8)

    diff = cv2.absdiff(gray, back)
    _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # labeling boxing
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(diff)

    for i in range(1, cnt):
        x, y, w, h, s = stats[i]
        
        if s < 75:
            continue

        cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 2)
    
    cv2.imshow('frame', frame)
    cv2.imshow('diff', diff)
    cv2.imshow('back', back)

    if cv2.waitKey(30) ==27:
        break

cap.release()
cv2.destroyAllWindows()