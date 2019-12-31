import numpy as np
import cv2

cap = cv2.VideoCapture(0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.createBackgroundSubtractorMOG2()
scale = 2

while(1):
    ret, frame = cap.read()
    if ret and frame is not None:
        frame = cv2.resize(frame, (frame.shape[1]*scale, frame.shape[0]*scale))
        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        cv2.imshow('frame', fgmask)
        # im = cv2.bitwise_and(frame, frame, mask=fgmask)
        # cv2.imshow('frame', im)
        k = cv2.waitKey(30) & 0xff
        if k == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
