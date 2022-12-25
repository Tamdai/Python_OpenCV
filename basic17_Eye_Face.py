import cv2

img = cv2.imread()

#อ่านไฟล์สำหรับ classification
face_cascade=cv2.CascadeClassifier()
eye_cascade=cv2.CascadeClassifier()

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

face_detect = face_cascade.detectMultiScale(gray_img,1.1,4)

eye_detect = eye_cascade.detectMultiScale(gray_img,1.1,4)

for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5)
    for (ax,ay,aw,ah) in eye_detect:
        cv2.rectangle(img,(ax,ay),(ax+aw,ay+ah),(255,0,0),thickness=5)

cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
