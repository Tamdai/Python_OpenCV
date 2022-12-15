#Export pic
import cv2

img = cv2.imread("image/cat.jpg") 
imgresize = cv2.resize(img,(400,400)) #ตัวแปร+กำหนดขนาด
cv2.imshow("Cat Cat",imgresize) #tital+pic

cv2.imwrite("output3.jpg",imgresize) #ส่งออกภาพ 

cv2.waitKey(0) #หน่วงเวลา
cv2.destroyAllWindows() #คืนค่า