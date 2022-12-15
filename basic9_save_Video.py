#Save Video
import cv2

cap = cv2.VideoCapture(0) #อ่านvideoกล้อง ()จำนวนกล้อง
fourcc = cv2.VideoWriter_fourcc(*'XVID') #

result = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480)) #ไฟล์ที่ส่งมา บึนทึกอะไรบ้าง

while (cap.isOpened()): #ตรวจสอบ loop สามารถใช้งานได้ ผ่านตัวแปร + ฟังชั่น  อ่านได้ ทำงานได้
    check , fraem = cap.read() #รับภาพจากกล้อง Frem : Frem ตัวแปร

    if check == True : #เช็คก่อนว่าวีดีโอยังเล่นไม่จบ
        cv2.imshow("Output",fraem) #แสดงผลออกมา แต่ละเฟรม
        result.write(fraem) #นำเอาค่าแดต่ละเฟรมเขียนลงไป
        if cv2.waitKey(1) & 0xFF == ord("e"): #(กดตัว e = ตัดจบ) หยุดถ่ายvideo
            break #out loop

result.release() #รวบรวมไฟล์
cap.release() #เคลีย
cv2.destroyAllWindows()