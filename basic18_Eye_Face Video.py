import cv2 

cap = cv2.VideoCapture("image/Mark.mp4")

face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface.xml")
eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

while (cap.isOpened()):
    check , frame = cap.read()
    if check == True :
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #ตรวจจับใบหน้า
        face_detect = face_cascade.detectMultiScale(gray_frame,1.3,4)
        #ตรวจจับดวงตา
        eye_detect = eye_cascade.detectMultiScale(gray_frame,1.3,4)
        
        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
            for(ex,ey,ew,eh) in eye_detect:
                cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,0,0),thickness=5)

        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()
