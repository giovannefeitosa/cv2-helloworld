##@ next: hsv.py
##@ prev: grayscale.py

# FOR MORE INFO ABOUT BLUR
# SEE:
#
# smoothing.py

import cv2

img = cv2.imread("assets/sample.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
img_blur = cv2.GaussianBlur(
    # the first parameter is an image
    img_gray,
    # the second parameter is a tuple (blur_x, blur_y)
    (7, 7),
    # the third parameter is standard deviation
    # it makes the image more blurred
    0,
);

cv2.imshow("Image", img_blur)

cv2.waitKey(0)
