##@ freestyle

import cv2

img = cv2.imread("assets/sample.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold value
# * lower, more dark
# * higher, more light
# * if the pixel value is lower than this value, it will be black
# * if the pixel value is higher than this value, it will be white
threshold_value = 90

threshold, thresh = cv2.threshold(
    img_gray,
    threshold_value,
    # max value
    255,
    # threshold type
    # * cv2.THRESH_BINARY
    # * cv2.THRESH_BINARY_INV
    # * cv2.THRESH_TRUNC
    # * cv2.THRESH_TOZERO
    # * cv2.THRESH_TOZERO_INV
    cv2.THRESH_BINARY,
)

# Invert threshold
threshold, thresh_inv = cv2.threshold(
    img_gray,
    threshold_value,
    255,
    cv2.THRESH_BINARY_INV,
)

cv2.imshow("Thresh", thresh)
cv2.imshow("Thresh inv", thresh_inv)

cv2.waitKey(0)
