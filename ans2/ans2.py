import numpy as np
import cv2
img = cv2.imread("imori.jpg").astype(np.float)
b, g, r = [img[:, :, i] for i in range(3)]

out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destoryAllWindows()
