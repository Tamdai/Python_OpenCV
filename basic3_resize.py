#ปรับขนาดภาพ

#อ่านภาพมาทำงาน
import cv2 #เรียกใช้งานคำสั่ง
img = cv2.imread("image/cat.jpg") #เรียกใช้งานรูป+โฟเดอร์
imgresize = cv2.resize(img,(400,400)) #ตัวแปร+กำหนดขนาด

#แสดงภาพ
cv2.imshow("Output",imgresize) #tital+pic
cv2.waitKey(delay=5000) #หน่วงเวลา
cv2.destroyAllWindows() #คืนค่า