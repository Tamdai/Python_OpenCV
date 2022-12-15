import cv2

img = cv2.imread("image/cat.jpg") 
imgresize = cv2.resize(img,(400,400)) 
cv2.imshow("Cat Cat",imgresize) 

cv2.imwrite("output3.jpg",imgresize) 

cv2.waitKey(0) 
cv2.destroyAllWindows() 
