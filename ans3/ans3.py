import numpy as np
import cv2
img = cv2.imread("imori.jpg").astype(np.float)
b, g, r = [img[:, :, i] for i in range(3)]

gray_img = 0.2126 * r + 0.7152 * g + 0.0722 * b
gray_img = gray_img.astype(np.uint8)

binary_img = gray_img.copy()
th = 128
binary_img[gray_img < th] = 0
binary_img[gray_img >= th] = 255

cv2.imwrite("out.jpg", binary_img)
cv2.imshow("result", binary_img)
cv2.waitKey(0)
cv2.destoryAllWindows()
