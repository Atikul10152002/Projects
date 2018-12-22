import cv2
import numpy as np
import hsv_val

sliderEnabled = False

def nothing(self):
 # empty function called by trackbars
    pass


class Calibrator:

    frame_width = 0
    frame_height = 0

    def writeHSV(self, file):
        # writes calibrated hsv value of target to text file
        hul = cv2.getTrackbarPos(hl, wnd) if sliderEnabled else hsv_val.hul
        huh = cv2.getTrackbarPos(hh, wnd) if sliderEnabled else hsv_val.huh
        sal = cv2.getTrackbarPos(sl, wnd) if sliderEnabled else hsv_val.sal
        sah = cv2.getTrackbarPos(sh, wnd) if sliderEnabled else hsv_val.sah
        val = cv2.getTrackbarPos(vl, wnd) if sliderEnabled else hsv_val.val
        vah = cv2.getTrackbarPos(vh, wnd) if sliderEnabled else hsv_val.vah
            

        file.write("hul = " + str(hul) + "\n")
        file.write("huh = " + str(huh) + "\n")
        file.write("sal = " + str(sal) + "\n")
        file.write("sah = " + str(sah) + "\n")
        file.write("val = " + str(val) + "\n")
        file.write("vah = " + str(vah) + "\n")

        file.close()

    def findPart(self, contours):
        # locates object and its centroid
        for c in contours:
            A = cv2.contourArea(c)
            M = cv2.moments(c)
            R = int((A/3.14)**(.5))
            # change this value if target is smaller/larger
            if A > 800:
                cv2.drawContours(res, [c], -1, (0, 255, 0), 3)
                # uses the contour's 'moment' to find centroid
                if M["m00"] != 0:
                    cX = int(M["m10"]/M["m00"])
                    cY = int(M["m01"]/M["m00"])
                else:
                    cX, cY = 0, 0
                cv2.circle(frame, (cX, cY), 10, (159, 159, 255), -1)
                cv2.circle(frame, (cX, cY), R, (255, 0, 0), 5)

    def getContours(self, frame):
        # anlyzes video feed and finds contours
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # read trackbar positions for each trackbar
        hul = cv2.getTrackbarPos(hl, wnd) if sliderEnabled else hsv_val.hul
        huh = cv2.getTrackbarPos(hh, wnd) if sliderEnabled else hsv_val.huh
        sal = cv2.getTrackbarPos(sl, wnd) if sliderEnabled else hsv_val.sal
        sah = cv2.getTrackbarPos(sh, wnd) if sliderEnabled else hsv_val.sah
        val = cv2.getTrackbarPos(vl, wnd) if sliderEnabled else hsv_val.val
        vah = cv2.getTrackbarPos(vh, wnd) if sliderEnabled else hsv_val.vah

        # define range of mask
        HSVLOW = np.array([hul, sal, val])
        HSVHIGH = np.array([huh, sah, vah])
        # create a mask for that range
        mask = cv2.inRange(hsv, HSVLOW, HSVHIGH)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        # use greyscale (single channel) to remove blobs and draw contours
        grey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        # blob removal
        #kernel = np.ones((5,5),np.uint8)
        #grey = cv2.erode(grey, kernel, iterations=1)
        #grey = cv2.dilate(grey, kernel, iterations=1)
        #grey = cv2.morphologyEx(grey, cv2.MORPH_OPEN, kernel)
        #grey = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, kernel)
        contours = cv2.findContours(
            grey, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
        return contours

    def getImage(self, frame):
        # applies mask using hsv trackbar values
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # read trackbar positions for each trackbar
        hul = cv2.getTrackbarPos(hl, wnd) if sliderEnabled else hsv_val.hul
        huh = cv2.getTrackbarPos(hh, wnd) if sliderEnabled else hsv_val.huh
        sal = cv2.getTrackbarPos(sl, wnd) if sliderEnabled else hsv_val.sal
        sah = cv2.getTrackbarPos(sh, wnd) if sliderEnabled else hsv_val.sah
        val = cv2.getTrackbarPos(vl, wnd) if sliderEnabled else hsv_val.val
        vah = cv2.getTrackbarPos(vh, wnd) if sliderEnabled else hsv_val.vah

        # define range of mask
        HSVLOW = np.array([hul, sal, val])
        HSVHIGH = np.array([huh, sah, vah])
        # create a mask for that range
        mask = cv2.inRange(hsv, HSVLOW, HSVHIGH)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        return res


cap = cv2.VideoCapture(0)
c = Calibrator()

# default color slider positions
hl_start = 0
hh_start = 179
sl_start = 0
sh_start = 255
vl_start = 0
vh_start = 255


# windows for sliders
cv2.namedWindow('Colorbars', cv2.WINDOW_AUTOSIZE)
hh = 'Hue High'
hl = 'Hue Low'
sh = 'Saturation High'
sl = 'Saturation Low'
vh = 'Value High'
vl = 'Value Low'
br = 'Blur'
wnd = 'Colorbars'

# (bar name, window name, min , max, argument)
if sliderEnabled:
    cv2.createTrackbar(hl, wnd, hl_start, 179, nothing)
    cv2.createTrackbar(hh, wnd, hh_start, 179, nothing)
    cv2.createTrackbar(sl, wnd, sl_start, 255, nothing)
    cv2.createTrackbar(sh, wnd, sh_start, 255, nothing)
    cv2.createTrackbar(vl, wnd, vl_start, 255, nothing)
    cv2.createTrackbar(vh, wnd, vh_start, 255, nothing)

frame_rate = 500 if sliderEnabled else 1
while(1):
    _, frame = cap.read()
    frame = cv2.resize(frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))
    contours = c.getContours(frame)
    res = c.getImage(frame)

    #frame = c.cropFrame(cropped, frame)
    res = c.getImage(frame)
    contours = c.getContours(frame)
    c.findPart(contours)

    cv2.imshow(wnd, frame)
    cv2.imshow('res', res)
    
    k = cv2.waitKey(frame_rate) & 0xFF
    if k == ord('s'):
        with open('hsv_val.py', 'a') as f:
            c.writeHSV(f)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
