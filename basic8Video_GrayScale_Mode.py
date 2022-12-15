#Video GrayScale Mode
import cv2

cap = cv2.VideoCapture("image/Video.mp4") #อ่านvideoกล้อง ()จำนวนกล้อง

while (cap.isOpened()): #ตรวจสอบ loop สามารถใช้งานได้ ผ่านตัวแปร + ฟังชั่น  อ่านได้ ทำงานได้
    check , fraem = cap.read() #รับภาพจากกล้อง Frem : Frem ตัวแปร

    if check == True : #เช็คก่อนว่าวีดีโอยังเล่นไม่จบ
        gray = cv2.cvtColor(fraem,cv2.COLOR_BGR2GRAY) #แปลงค่าสีจาก fraem ให้เป็น Gray
        cv2.imshow("Output",gray) #ภาพขาวดำจากตัวแปร gray มาแสดงผลภาพ

        if cv2.waitKey(1) & 0xFF == ord("e"): #เช็คผู้ใช้กดคีร์ ปิรอรับ key แล้ว (กดตัว e = ตัดจบ)
            break #out loop
    else : #เล่นวีดีโอไม่ค้างและปิดลงไป
        break

cap.release() #เคลีย
cv2.destroyAllWindows()