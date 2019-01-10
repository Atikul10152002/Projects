import cv2
import numpy as np

pnts = []
window, preswin = ["Frame", "PT"]
cv2.namedWindow(window, cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(0)


def main():
    global pnts
    while 1:
        _, frame = cap.read()
        frame = cv2.resize (frame, (frame.shape[1]//2, frame.shape[0]//2))
        cleanFrame = frame.copy()

        cv2.setMouseCallback(window, mouse_click)
        list(map(lambda x: cv2.circle(frame, tuple(x), 3, (0, 0, 255), -1), pnts))
        if len(pnts) == 4:
            pts = np.array(pnts)
            cv2.polylines(frame, np.int32(
                [np.array([*pts])]), 1, (0, 255, 0), 1)
            output = four_point_transform(cleanFrame, pts)
            cv2.imshow(preswin, output)

        else:
            cv2.destroyWindow(preswin)

        cv2.imshow(window, frame)

        key = cv2.waitKey(1)
        if key == ord("q"): break
        elif key == ord("c"):
            pnts = []
            pts = None


    cap.release()
    cv2.destroyAllWindows()



def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(pnts) < 4:
            pnts.append([x, y])


def four_point_transform(image, pts, inverse: bool=False):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped



if __name__ == "__main__":
    main()
