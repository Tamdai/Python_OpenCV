import cv2

cap = cv2.VideoCapture("image/Video.mp4") 

while (cap.isOpened()): 
    check , fraem = cap.read() 

    if check == True : 
        gray = cv2.cvtColor(fraem,cv2.COLOR_BGR2GRAY) 
        cv2.imshow("Output",gray) 

        if cv2.waitKey(1) & 0xFF == ord("e"): 
            break #out loop
    else : 
        break

cap.release()
cv2.destroyAllWindows()
