##@ freestyle

import cv2
import numpy as np

img = cv2.imread("assets/sample.jpg")

b,g,r = cv2.split(img)
blank = np.zeros(img.shape[:2], dtype=np.uint8)

cv2.imshow("blue", cv2.merge((b, blank, blank)))
cv2.imshow("green", cv2.merge((blank, g, blank)))
cv2.imshow("red", cv2.merge((blank, blank, r)))
cv2.imshow("merged 2 channels", cv2.merge((b, blank, r)))

cv2.waitKey(0)
