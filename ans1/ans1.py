import cv2
import numpy as n

img = cv2.imread("imori.jpg")
b, g, r = [img[:, :, i] for i in range(3)]

out = img.copy()
out[:, :, 0] = r
out[:, :, 1] = g
out[:, :, 2] = b

cv2.imwrite('out.jpg', out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
