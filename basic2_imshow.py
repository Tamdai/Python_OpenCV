#แสดงผลภาพ imshow
import cv2
img = cv2.imread("image/cat.jpg")

cv2.imshow("Output",img)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()