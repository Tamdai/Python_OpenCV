import cv2 

cap = cv2.VideoCapture("image/Video.mp4")

face_cascade=cv2.CascadeClassifier("Detect/haarcascade_frontalface.xml")

while (cap.isOpened()):
    check , frame = cap.read()
    if check == True :
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
        
        face_detect = face_cascade.detectMultiScale(gray_img,1.2,5)
       
        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
            cv2.imshow("Output",frame)

        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()
