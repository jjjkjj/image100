import cv2
import numpy as n

img = cv2.imread("imori.jpg")
cv2.imwrite('out.jpg', img)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
