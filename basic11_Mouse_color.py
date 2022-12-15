#ตรวจจับค่าสี Mouse
import cv2
img = cv2.imread("image/color.jpg")

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:  #เช็ค event ทำอะไรบ้าง 5 ตัวหลัก
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]

        text = str(blue)+","+str(green)+","+str(red)    #แสดงค่าสี b,g,r
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),cv2.LINE_4) #แสดงข้อความออกมา FONT_HERSHEY_SIMPLEX ชื่อfoint,1 size,(0.0.255 red) LINE_4 หนา
        cv2.imshow("Output",img)

#แสดงภาพ
cv2.imshow("Output",img)
#ทำงานกับ Mouse
cv2.setMouseCallback("Output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()