#เปิดวีดีโอด้วย OpenCV
import cv2

cap = cv2.VideoCapture("image/Video.mp4") #อ่านvideoกล้อง ()จำนวนกล้อง

while (cap.isOpened()): #ตรวจสอบ loop สามารถใช้งานได้ ผ่านตัวแปร + ฟังชั่น  อ่านได้ ทำงานได้
    check , fraem = cap.read() #รับภาพจากกล้อง Frem : Frem ตัวแปร

    if check == True : #เช็คก่อนว่าวีดีโอยังเล่นไม่จบ ให้แสดงผล 
        cv2.imshow("Output",fraem) #ภาพแต่ละfreamที่อ่าน มาแสดงผลภาพ

        if cv2.waitKey(1) & 0xFF == ord("e"): #เช็คผู้ใช้กดคีร์ ปิรอรับ key แล้ว (คีร์คือกดตัว e ไหม = ตัดจบ)
            break #out loop
    else : #เล่นวีดีโอไม่ค้างและปิดลงไป
        break

cap.release() #เคลีย
cv2.destroyAllWindows()