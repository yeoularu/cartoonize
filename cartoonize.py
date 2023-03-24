import cv2 as cv

video_source = 'sample.mp4'


def cartoonize(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    blured = cv.GaussianBlur(gray, (13, 13), 0)

    edges = cv.adaptiveThreshold(
        blured, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 3)

    filtered = cv.bilateralFilter(image, 5, 500, 500)

    cartoon = cv.bitwise_and(filtered, filtered, mask=edges)
    return cartoon


cap = cv.VideoCapture(video_source)
while (cap.isOpened()):
    ret, frame = cap.read()
    cartoon = cartoonize(frame)
    cv.imshow("press ESC key to exit", cartoon)

    key = cv.waitKey(1) & 0xFF
    if key == 27:  # esc
        break

cap.release()
cv.destroyAllWindows()
