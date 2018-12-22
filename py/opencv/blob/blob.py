import cv2
import numpy as np


class Calibrator:

    frame_width = 0
    frame_height = 0

    def writeHSV(self, file):
        '''
        writes calibrated hsv value of target to text file
        writeHSV(self, file) -> None
        '''

        # * read trackbar positions for each trackbar. The function returns the current position of the specified trackbar
        # ? getTrackbarPos(trackbarname, winname) -> retval
        hul = cv2.getTrackbarPos(hl, wnd)
        huh = cv2.getTrackbarPos(hh, wnd)
        sal = cv2.getTrackbarPos(sl, wnd)
        sah = cv2.getTrackbarPos(sh, wnd)
        val = cv2.getTrackbarPos(vl, wnd)
        vah = cv2.getTrackbarPos(vh, wnd)

        # * Appending the final HSV values to the `file`
        file.write("hul = " + str(hul) + "\n")
        file.write("huh = " + str(huh) + "\n")
        file.write("sal = " + str(sal) + "\n")
        file.write("sah = " + str(sah) + "\n")
        file.write("val = " + str(val) + "\n")
        file.write("vah = " + str(vah) + "\n")
        file.close()

    def findPart(self, contours):
        '''
        locates object and its centroid
        findPart(self, contours) -> None
        '''
        for c in contours:

            # ? contourArea(contour[, oriented]) -> retval
            # * The function computes a contour area. Similarly to moments , the area is computed using the Green. formula. Thus, the returned area and the number of non-zero pixels, if you draw the contour using. \  # drawContours or \#fillPoly , can be different. Also, the function will most certainly give a wrong. results for contours with self-intersections
            A = cv2.contourArea(c)

            # ? moments(array[, binaryImage]) -> retval
            # * The function computes moments, up to the 3rd order, of a vector shape or a rasterized shape. The results are returned in the structure cv: : Moments.
            M = cv2.moments(c)
            R = int((A/3.14)**(.5))
            # ? change this value if target is smaller/larger
            if A > 800:

                # ? drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) -> image
                cv2.drawContours(res, [c], -1, (0, 255, 0), 3)
                # uses the contour's 'moment' to find centroid
                if M["m00"] != 0:
                    cX = int(M["m10"]/M["m00"])
                    cY = int(M["m10"]/M["m00"])
                else:
                    cX, cY = 0, 0

                # ? circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> img
                # * The function cv::circle draws a simple or filled circle with a given center and radius
                cv2.circle(frame, (cX, cY), 10, (159, 159, 255), -1)
                cv2.circle(frame, (cX, cY), R, (255, 0, 0), 5)

    def getContours(self, frame):
        '''
        analyzes video feed and finds contours
        getContours(self, frame) -> contours
        '''
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        # ? cvtColor(src, code[, dst[, dstCn]]) -> dst
        # * The function converts an input image from one color space to another
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # * read trackbar positions for each trackbar. The function returns the current position of the specified trackbar
        # ? getTrackbarPos(trackbarname, winname) -> retval
        hul = cv2.getTrackbarPos(hl, wnd)
        huh = cv2.getTrackbarPos(hh, wnd)
        sal = cv2.getTrackbarPos(sl, wnd)
        sah = cv2.getTrackbarPos(sh, wnd)
        val = cv2.getTrackbarPos(vl, wnd)
        vah = cv2.getTrackbarPos(vh, wnd)
        # define range of mask
        HSV_LOW = np.array([hul, sal, val])
        HSV_HIGH = np.array([huh, sah, vah])
        # create a mask for that range
        mask = cv2.inRange(hsv, HSV_LOW, HSV_HIGH)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # ? cvtColor(src, code[, dst[, dstCn]]) -> dst
        # * use greyscale (single channel) to remove blobs and draw contours
        # * The function converts an input image from one color space to another
        grey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        # blob removal
        #kernel = np.ones((5,5),np.uint8)
        #grey = cv2.erode(grey, kernel, iterations=1)
        #grey = cv2.dilate(grey, kernel, iterations=1)
        #grey = cv2.morphologyEx(grey, cv2.MORPH_OPEN, kernel)
        #grey = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, kernel)

        # ? findContours(image, mode, method[, contours[, hierarchy[, offset]]]) -> image, contours, hierarchy
        # * The function retrieves contours from the binary image using the algorithm passed as an argument
        contours = cv2.findContours(
            grey, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
        return contours

    def getImage(self, frame):
        '''
        applies mask using hsv trackbar values
        getImage(self, frame) -> res
        '''

        # ? GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst
        frame = cv2.GaussianBlur(frame, (5, 5), 0)

        # ? cvtColor(src, code[, dst[, dstCn]]) -> dst
        # * The function converts an input image from one color space to another
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # * read trackbar positions for each trackbar. The function returns the current position of the specified trackbar
        # ? getTrackbarPos(trackbarname, winname) -> retval
        hul = cv2.getTrackbarPos(hl, wnd)
        huh = cv2.getTrackbarPos(hh, wnd)
        sal = cv2.getTrackbarPos(sl, wnd)
        sah = cv2.getTrackbarPos(sh, wnd)
        val = cv2.getTrackbarPos(vl, wnd)
        vah = cv2.getTrackbarPos(vh, wnd)
        # define range of mask
        HSVLOW = np.array([hul, sal, val])
        HSVHIGH = np.array([huh, sah, vah])
        # create a mask for that range
        mask = cv2.inRange(hsv, HSVLOW, HSVHIGH)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        return res


cap = cv2.VideoCapture(1)
c = Calibrator()

# * default color slider positions
hl_start = 0
hh_start = 179
sl_start = 0
sh_start = 255
vl_start = 0
vh_start = 255

# * windows for sliders
# ? namedWindow(winname[, flags]) -> None
cv2.namedWindow('Colorbars', cv2.WINDOW_AUTOSIZE)
hh = 'Hue High'
hl = 'Hue Low'
sh = 'Saturation High'
sl = 'Saturation Low'
vh = 'Value High'
vl = 'Value Low'
br = 'Blur'
wnd = 'Colorbars'


def nothing(x):
    # * deals with onChange argument of cv2.createTrackbar()
    return x


# ? createTrackbar(trackbarName, windowName, value, count, onChange) -> None
cv2.createTrackbar(hl, wnd, hl_start, 179, nothing)
cv2.createTrackbar(hh, wnd, hh_start, 179, nothing)
cv2.createTrackbar(sl, wnd, sl_start, 255, nothing)
cv2.createTrackbar(sh, wnd, sh_start, 255, nothing)
cv2.createTrackbar(vl, wnd, vl_start, 255, nothing)
cv2.createTrackbar(vh, wnd, vh_start, 255, nothing)

while 1:
    _, frame = cap.read()

    # ? resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) -> dst
    # * The function resize resizes the image src down to or up to the specified size
    frame = cv2.resize(frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))

    contours = c.getContours(frame)
    res = c.getImage(frame)

    #frame = c.cropFrame(cropped, frame)
    # res = c.getImage(frame)

    contours = c.getContours(frame)
    c.findPart(contours)

    # ? imshow(winname, mat) -> None
    cv2.imshow(wnd, frame)
    cv2.imshow('res', res)

    # ? waitKey([, delay]) -> retval
    # * The function waitKey waits for a key event infinitely or milliseconds, when the argument is positive
    k = cv2.waitKey(5) & 0xFF

    if k == ord('s'):
        with open('hsv_val.txt', 'a') as f:
            c.writeHSV(f)

    elif k == ord('q'):
        break

# ? destroyAllWindows() -> None
# * The function destroyAllWindows destroys all of the opened HighGUI windows
cv2.destroyAllWindows()

# ? Releases the Video Capture
cap.release()
