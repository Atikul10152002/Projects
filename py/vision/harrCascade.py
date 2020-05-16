#!/usr/bin/env python3

import cv2

face = cv2.CascadeClassifier(
    '/Users/abir/Github/prog_lang/py/vision/face_cas.xml')
#eye = cv2.CascadeClassifier(
#    '/Users/abir/Github/prog_lang/py/vision/eye_cas.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    if ret:
        # -- Detect faces

        faces = face.detectMultiScale(frame)
        for (x, y, w, h) in faces:
            center = (x + w//2, y + h//2)
            frame = cv2.ellipse(frame, center, (w//2, h//2),
                                0, 0, 360, (255, 0, 255), 4)
            faceROI = frame[y:y+h, x:x+w]
            # -- In each face, detect eyes
 #           eyes = eye.detectMultiScale(faceROI)
 #           for (x2, y2, w2, h2) in eyes:
 #               eye_center = (x + x2 + w2//2, y + y2 + h2//2)
 #               radius = int(round((w2 + h2)*0.25))
 #               frame = cv2.circle(frame, eye_center, radius, (255, 0, 0), 4)
        k = cv2.waitKey(30) & 0xff
        if k == ord('q'):
            break
        cv2.imshow('Capture - Face detection', frame)

cap.release()
