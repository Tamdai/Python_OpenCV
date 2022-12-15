#เปิดกล้องด้วย OpenCV
import cv2

cap = cv2.VideoCapture(0) #อ่านvideoกล้อง ()จำนวนกล้อง

while (True): #ตรวจสอบ
    check , fraem = cap.read() #รับภาพจากกล้อง Frem : Frem
    cv2.imshow("Output",fraem) #ภาพแต่ละfreamที่อ่าน มาแสดงผล

    if cv2.waitKey(1) & 0xFF == ord("e"): #เช็คผู้ใช้กดคีร์ ปิดรอรับ key แล้ว คีร์คือกดตัว e ไหม
        break #out loop

cap.release() #เคลีย
cv2.destroyAllWindows()

