import cv2
import numpy as np
import timeit


window = "MainFrame"
cv2.namedWindow(window)

frame = cv2.imread('/Users/atikul/GitHub/prog_lang/py/retrofit/test_img.jpg')
# cap1 = cv2.VideoCapture(0)
# cap2 = cv2.VideoCapture(1)

def main():
    while (1):
        _, source1 = [1, frame]
        _, source2 = [1, frame]
        _, source3 = [1, frame]
        _, source4 = [1, frame]

        out = combineFrames(source1, source2, source3, source4)
        out = resize(out, .3)

        cv2.imshow(window, out)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    # cap.release()
    cv2.destroyAllWindows()


def nothing(*a, **K): pass


def prespectiveShift(img, bottomRange):
    IMAGE_H, IMAGE_W = size(img)

    src = np.array([[0, IMAGE_H], [IMAGE_W, IMAGE_H],
                    [0, 0], [IMAGE_W, 0]], dtype="float32")
    dst = np.array([[(IMAGE_W//2)-bottomRange, IMAGE_H], [(IMAGE_W//2)+bottomRange, IMAGE_H], [
        0, 0], [IMAGE_W, 0]], dtype="float32")
    M = cv2.getPerspectiveTransform(src, dst)

    npslice = 610
    cv2.createTrackbar("slice", window, npslice, 1000, nothing)
    npslice = cv2.getTrackbarPos("slice", window)
    img = img[npslice:(npslice+IMAGE_H), 0:IMAGE_W]

    return cv2.warpPerspective(img, M, (IMAGE_W, IMAGE_H))


def createAlphaChannel(src):
    src = cv2.cvtColor(src, cv2.COLOR_BGR2RGBA)
    src[np.all(src == [0, 0, 0, 255], axis=2)] = [0, 0, 0, 0]
    return src


def resize(src, ratio):
    src = cv2.resize(src, (int(src.shape[1]*ratio), int(src.shape[0]*ratio)))
    return src

def size(src): return src.shape[:2]

def rotate(src, angle):
    if angle == 90:
        src = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
    elif angle == -90:
        src = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif angle == 180:
        src = cv2.rotate(src, cv2.ROTATE_180)
    return src

def combineFrames(topView, leftView, bottomView, rightView):

    bottomRange = 80
    cv2.createTrackbar("bottomRange", window, bottomRange, 1000, nothing)
    bottomRange = cv2.getTrackbarPos("bottomRange", window)

    # functions
    topView = prespectiveShift(topView, bottomRange)

    leftView = prespectiveShift(leftView, bottomRange)
    leftView = rotate(leftView, -90)

    bottomView = prespectiveShift(bottomView, bottomRange)
    bottomView = rotate(bottomView, 180)

    rightView = prespectiveShift(rightView, bottomRange)
    rightView = rotate(rightView, 90)

    # 4 channels
    topView = createAlphaChannel(topView)
    leftView = createAlphaChannel(leftView)
    bottomView = createAlphaChannel(bottomView)
    rightView = createAlphaChannel(rightView)

    topHeight, topWidht = size(topView)
    leftHeight, leftWidth = size(leftView)
    bottomHeight, bottomWidth = size(bottomView)
    rightHeight, rightWidth = size(rightView)

    overlay1 = np.zeros((max(topHeight, leftHeight), topWidht, 4), dtype="uint8")
    overlay2 = overlay1.copy()
    overlay3 = overlay1.copy()
    overlay4 = overlay1.copy()

    overlay1[0:topHeight, 0:topWidht] = topView
    overlay2[0:leftHeight, 0:leftWidth] = leftView
    overlay3[overlay3.shape[0]-bottomHeight:overlay3.shape[0], 0:bottomWidth] = bottomView
    overlay4[0:rightHeight, overlay4.shape[1]-rightWidth:overlay4.shape[0]] = rightView

    out = cv2.bitwise_or(overlay1, overlay2)
    out = cv2.bitwise_or(out, overlay3)
    out = cv2.bitwise_or(out, overlay4)

    cv2.cvtColor(out, cv2.COLOR_RGBA2BGR)

    return out

if __name__ == "__main__":
    main()
