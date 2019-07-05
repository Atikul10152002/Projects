#!/usr/bin/env python3

import cv2
import numpy as np
import requests
import random
from sys import argv
from matplotlib import pyplot as plt

template_image =cv2.imread('dot.jpg',0)
# url ='http://'+str(argv[1])+'/shot.jpg'
# user = str(argv[2])
# password = str(argv[3])
# data = urllib.parse.urlencode({ 'username': user,'password': password })
video = cv2.VideoCapture(0)

img_rgb = sample_image.copy()
template = template_image
w, h = template.shape[::-1]

wnd = "window"
window = cv2.namedWindow(wnd)
cv2.createTrackbar("thr", wnd, 80, 100, lambda x: x)
face = cv2.CascadeClassifier(
        'face_cas.xml')
eye = cv2.CascadeClassifier(
        'eye_cas.xml')
while 1:
    # key = cv2.waitKey(1)
    # req = requests.get(url, auth=(user, password))
    # if key==ord("c"):
    # imgResp=urllib.request.urlopen(url, data)
    imgNp=np.array(bytearray(req.content),dtype=np.uint8)
    img_rgb=cv2.imdecode(imgNp,-1)

    img_rgb = cv2.resize(img_rgb,(int(img_rgb.shape[1]//2), int(img_rgb.shape[0]//2)))
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(img_gray, 1.5, 3)
    eyes = eye.detectMultiScale(img_gray, 1.5, 3)
    # smiles = smile.detectMultiScale(gray, 1.5, 3)
    # * drawing the rectanges
    for (x, y, w, h) in faces:
        # ? rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
        #* The function cv::rectangle draws a rectangle outline or a filled rectangle whose two opposite corners
        cv2.rectangle(img_rgb, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # for (sx, sy, sw, sh) in smiles:
        #     cv2.rectangle(frame, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)
        # * drawing both eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(img_rgb, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)


    # res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    # # threshold = .55
    # threshold = cv2.getTrackbarPos("thr", wnd)/100

    # loc = np.where( res >= threshold)
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,min(255-int(pt[1]),255), min(int(pt[1]), 255)), 1)

    # cv2.imshow('res.png',img_rgb)
    cv2.imshow(wnd,img_rgb)
    if key==ord("q"):
        break
    if key==ord("s"):
        cv2.imwrite("res"+str(random.random())+".png", img_rgb)

# video.release()