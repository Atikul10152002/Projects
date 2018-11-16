import cv2
import numpy as np
video = cv2.VideoCapture(1)

params = cv2.SimpleBlobDetector_Params()

# Change thresholds

params.minThreshold = 0
params.maxThreshold = 256

# Filter by Area.
params.filterByArea = True
params.minArea = 50

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.01

# Filter by Convexity
params.filterByConvexity = 0
params.minConvexity = 0.5

# Filter by Inertia
params.filterByInertia = 0
params.minInertiaRatio = 0.5

detector = cv2.SimpleBlobDetector_create(params)





a = 0
while 1:
    a += 1
    check, frame = video.read()
    frame = cv2.resize(frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([30, 0, 0])
    uppore_orange = np.array([255,255,255])

    mask = cv2.inRange(hsv, lower_orange, uppore_orange)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    # imgkeypoints = cv2.drawKeypoints(frame, keypoints, np.array(
        # []), (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow("mask", mask)
    cv2.imshow("res", res)


    key = cv2.waitKey(1)
    if key == ord("q"):
        break


video.release()
cv2.destroyAllWindows()
