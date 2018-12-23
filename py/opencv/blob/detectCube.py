import cv2
import numpy as np
import hsv_val

sliderEnabled = True

class cvPipeline:
    # * default color slider positions
    hueLowStart = 0
    hueHighStart = 255
    saturationLowStart = 0
    saturationHighStart = 255
    valueLowStart = 0
    valueHighStart = 255
    hsvValueMax = 255

    # * reduced frame rate to avoid lag issues of less powerful computers
    # framesPerSecond = 2 if sliderEnabled else 1
    framesPerSecond = 60

    # * slider names
    hh = 'Hue High'
    hl = 'Hue Low'
    sh = 'Saturation High'
    sl = 'Saturation Low'
    vh = 'Value High'
    vl = 'Value Low'
    br = 'Blur'
    wnd = 'Colorbars'
    # kernelSize = "kernel_size"
    # kernelDivision = "kernel_division"

    def __init__(self):
        # * windows for sliders
        # ? namedWindow(winname[, flags]) -> None
        cv2.namedWindow(self.wnd, cv2.WINDOW_AUTOSIZE)

        # ? (bar name, window name, min , max, argument)
        if sliderEnabled:
            cv2.createTrackbar(self.hl, self.wnd, self.hueLowStart,
                               self.hsvValueMax, self.nothing)
            cv2.createTrackbar(self.hh, self.wnd,
                               self.hueHighStart, self.hsvValueMax, self.nothing)
            cv2.createTrackbar(self.sl, self.wnd,
                               self.saturationLowStart, self.hsvValueMax, self.nothing)
            cv2.createTrackbar(self.sh, self.wnd,
                               self.saturationHighStart, self.hsvValueMax, self.nothing)
            cv2.createTrackbar(self.vl, self.wnd,
                               self.valueLowStart, self.hsvValueMax, self.nothing)
            cv2.createTrackbar(self.vh, self.wnd,
                               self.valueHighStart, self.hsvValueMax, self.nothing)

        # * Testing with different values to denoise
        # cv2.createTrackbar(kernelSize, wnd, 0, 10, nothing)
        # cv2.createTrackbar(kernelDivision, wnd, 1, 25, nothing)


    def run(self, video):
        self.cap = video

        while(self.cap.isOpened()):
            try:
                self._, self.frame = self.cap.read()
                self.frame = cv2.flip(self.frame, 1)

                # * resizing the frame to better fit the screen
                self.frame = cv2.resize(self.frame,
                                        (int(self.frame.shape[1]/2),
                                        int(self.frame.shape[0]/2)))

                # * read trackbar positions for each trackbar. The function returns the current position of the specified trackbar
                # ? getTrackbarPos(trackbarname, winname) -> retval
                hueLow = cv2.getTrackbarPos(
                    self.hl, self.wnd) if sliderEnabled else hsv_val.hueLow
                hueHigh = cv2.getTrackbarPos(
                    self.hh, self.wnd) if sliderEnabled else hsv_val.hueHigh
                saturationLow = cv2.getTrackbarPos(
                    self.sl, self.wnd) if sliderEnabled else hsv_val.saturationLow
                saturationHigh = cv2.getTrackbarPos(
                    self.sh, self.wnd) if sliderEnabled else hsv_val.saturationHigh
                valueLow = cv2.getTrackbarPos(
                    self.vl, self.wnd) if sliderEnabled else hsv_val.valueLow
                valueHigh = cv2.getTrackbarPos(
                    self.vh, self.wnd) if sliderEnabled else hsv_val.valueHigh

                self.contours = self.getContours(
                    self.frame, hueLow, hueHigh, saturationLow, saturationHigh, valueLow, valueHigh)
                if sliderEnabled:
                    self.res = self.getImage(
                        self.frame, hueLow, hueHigh, saturationLow, saturationHigh, valueLow, valueHigh)
                    #frame = c.cropFrame(cropped, frame)
                    self.findPart(self.contours)
                    cv2.imshow('res', self.res)
                else:
                    self.frame = self.getImage(
                        self.frame, hueLow, hueHigh, saturationLow, saturationHigh, valueLow, valueHigh)
                    #frame = c.cropFrame(cropped, frame)
                    self.findPart(self.contours)
                cv2.imshow(self.wnd, self.frame)

                key = cv2.waitKey(1000//self.framesPerSecond)
                if key == ord('s') and sliderEnabled:
                    self.writeHSV(hueLow, hueHigh, saturationLow, saturationHigh, valueLow, valueHigh)
                if key == ord('q'):
                    self.cap.release()
                    break
            except Exception as e:
                print(e)

    def nothing(self, *a, **k):
        '''
        empty function called by trackbars
        '''
        pass

    def writeHSV(self, hueLow, hueHigh, saturationLow, saturationHigh, valueLow, valueHigh):
        '''
        writes calibrated hsv value of target to text file
        writeHSV(self) -> None
        '''

        # * Appending the final HSV values to the `file`
        with open('hsv_val.py', 'a') as file:
            file.write('hueLow = ' + str(hueLow) + '\n')
            file.write('hueHigh = ' + str(hueHigh) + '\n')
            file.write('saturationLow = ' + str(saturationLow) + '\n')
            file.write('saturationHigh = ' + str(saturationHigh) + '\n')
            file.write('valueLow = ' + str(valueLow) + '\n')
            file.write('valueHigh = ' + str(valueHigh) + '\n')

            file.close()

    def findPart(self, contours):
        # locates object and its centroid
        for c in contours:
            # ? contourArea(contour[, oriented]) -> retval
            # * The function computes a contour area. Similarly to moments , the area is computed using the Green. formula. Thus, the returned area and the number of non-zero pixels, if you draw the contour using. \  # drawContours or \#fillPoly , can be different. Also, the function will most certainly give a wrong. results for contours with self-intersections
            self.A = cv2.contourArea(c)

            # ? moments(array[, binaryImage]) -> retval
            # * The function computes moments, up to the 3rd order, of a vector shape or a rasterized shape. The results are returned in the structure cv: : Moments.
            self.M = cv2.moments(c)
            #* Radius = sqrt(Area * Pi)
            self.R = int((self.A/3.14)**(.5))
            # ? change this value if target is smaller/larger
            if self.A > 10000:

                # ? drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) -> image
                cv2.drawContours(self.res, [c], -1, (0, 255, 0), 3)
                # * uses the contour's 'moment' to find centroid
                if self.M['m00'] != 0:
                    cX = int(self.M['m10']/self.M['m00'])
                    cY = int(self.M['m01']/self.M['m00'])
                else:
                    cX, cY = 0, 0
                # ? circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> img
                # * The function cv::circle draws a simple or filled circle with a given center and radius
                # * Centroid center circle
                # print("Blob center", cX,cY)
                cv2.circle(self.frame, (cX, cY), 10, (159, 159, 255), -1)
                # * Centroid surrounding circle
                cv2.circle(self.frame, (cX, cY), self.R, (255, 0, 0), 5)

    def getContours(self, frame, hueLow, hueHigh, saturationLow, saturationHigh, valueLow, valueHigh):
        '''
        analyzes video feed and finds contours
        getContours(self, frame) -> contours
        '''
        # ? GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst
        self.frame = cv2.GaussianBlur(frame, (5, 5), 0)
        # ? cvtColor(src, code[, dst[, dstCn]]) -> dst
        # * The function converts an input image from one color space to another
        self.hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of mask
        self.HSV_LOW = np.array([hueLow, saturationLow, valueLow])
        self.HSV_HIGH = np.array([hueHigh, saturationHigh, valueHigh])
        # create a mask for that range
        self.mask = cv2.inRange(self.hsv, self.HSV_LOW, self.HSV_HIGH)
        self.res = cv2.bitwise_and(self.frame, self.frame, mask=self.mask)

        # ? cvtColor(src, code[, dst[, dstCn]]) -> dst
        # * use greyscale (single channel) to remove blobs and draw contours
        # * The function converts an input image from one color space to another
        self.grey = cv2.cvtColor(self.res, cv2.COLOR_BGR2GRAY)
        # blob removal

        self.kernel = np.ones((0, 0), np.uint8)/25
        # kernel = np.ones((cv2.getTrackbarPos(kernelSize, wnd) ,cv2.getTrackbarPos(kernelSize, wnd) ),np.uint8)/cv2.getTrackbarPos(kernelDivision, wnd)

        #grey = cv2.erode(grey, kernel, iterations=1)
        self.grey = cv2.dilate(self.grey, self.kernel, iterations=1)
        self.grey = cv2.morphologyEx(self.grey, cv2.MORPH_OPEN, self.kernel)
        # grey = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, kernel)

        # ? findContours(image, mode, method[, contours[, hierarchy[, offset]]]) -> image, contours, hierarchy
        # * The function retrieves contours from the binary image using the algorithm passed as an argument
        self.contours = cv2.findContours(
            self.grey, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
        return self.contours

    def getImage(self, frame, hueLow, hueHigh, saturationLow, saturationHigh, valueLow, valueHigh):
        '''
        applies mask using hsv trackbar values
        getImage(self, frame) -> res
        '''
        # ? GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        # ? cvtColor(src, code[, dst[, dstCn]]) -> dst
        # * The function converts an input image from one color space to another
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of mask
        self.HSV_LOW = np.array([hueLow, saturationLow, valueLow])
        self.HSV_HIGH = np.array([hueHigh, saturationHigh, valueHigh])
        # create a mask for that range
        self.mask = cv2.inRange(hsv, self.HSV_LOW, self.HSV_HIGH)
        self.res = cv2.bitwise_and(frame, frame, mask=self.mask)
        return self.res


cam = cvPipeline()

vidFeed = cv2.VideoCapture(1)
cam.run(vidFeed)

vidFeed.release()
cv2.destroyAllWindows()
# self.out.release()
