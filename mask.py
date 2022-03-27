##@: freestyle

import cv2
import numpy as np

img = cv2.imread("assets/sample.jpg")

# create mask
blank = np.zeros(img.shape[:2], dtype=np.uint8)
mask = cv2.circle(
    blank,
    # center point (x, y)
    #
    # (img.shape[1]//2, img.shape[0]//2),
    (500, 360),
    # radius
    100,
    # color
    255,
    # thickness
    -1,
)

# apply mask
img_masked = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Image", img_masked)

cv2.waitKey(0)

