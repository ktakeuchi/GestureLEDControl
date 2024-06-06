import cv2
import time
import HandTrackingModule as htm
import math
import numpy as np
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
arduino = SerialObject(portNo="COM15",digits=3,baudRate=9600)
pTime = 0
detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(img, (x1,y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255, 0, 255),3 )
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)
        brightness = np.interp(length, [20, 200], [0, 255])
        brightness = np.round(brightness)
        cv2.putText(img, str(brightness), (cx, cy), cv2.FONT_HERSHEY_DUPLEX, 1,
(255, 0, 0), 3)
        
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.imshow("liveshow", img)
    cv2.waitKey(1)
