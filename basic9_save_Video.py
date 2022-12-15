import cv2

cap = cv2.VideoCapture(0) 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 

result = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480)) 

while (cap.isOpened()): 
    check , fraem = cap.read() 
    
    if check == True : 
        cv2.imshow("Output",fraem)
        result.write(fraem) 
        if cv2.waitKey(1) & 0xFF == ord("e"): 
            break 

result.release() 
cap.release() 
cv2.destroyAllWindows()
