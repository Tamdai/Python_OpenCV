import cv2

#อ่านภาพ
img = cv2.imread("image/girl.jpg")

#อ่านไฟล์สำหรับ classification
eye_cascade=cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #แปลงภาพสี เป็น ขาวดำ

#จำแนกดวงตา แสดงตำแหน่งเจอดวงตา ตามที่ใช้งาน
scaleFactor = 1.1  #ย่อขนาดของภาพลง 
minNeighber = 3    #ทำซ้ำตำแหน่งแสดงใบหน้า คำนนค่าซ้ำๆกัน จุดที่ใกล้เคียงใบหน้า ถี่สุด 0
eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber) #ส่งภาพ gray

#แสดงตำแหน่งที่เจอใบหน้า
for (x,y,w,h) in eye_detect: #วันลูป x,y จุดเริ่มต้น ,w,h จุดสุดท้าย อ่านและส่งกลับมา
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5) #แสดงตำแหน่งที่เจอใบหน้า หาใบหน้าเจอ สร้างกล่องสี่เหลี่ยม (0,255,0) สีกล่อง thickness=5 ความหนา

#แสดงภาพ
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()