import cv2

img = cv2.imread("image/girl.jpg")

eye_cascade=cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

scaleFactor = 1.1  
minNeighber = 3    
eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber) 

for (x,y,w,h) in eye_detect: 
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5) 

cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
