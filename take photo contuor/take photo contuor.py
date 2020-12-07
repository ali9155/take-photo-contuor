import cv2
import numpy as np

c_ = 0
FILE_NAME="Class_.jpg"
video = cv2.VideoCapture(0)
while True: 
    #img_1 = cv2.imread("0.jpg")

    _, frame = video.read()
    #frame_1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",frame)
    #canny=cv2.Canny(frame,100,200)
    #cv2.imshow("Canny",canny)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
       cv2.destroyAllWindows()
       break
    if key == ord('s'):
    #if (M0) ==[True]:  
        cv2.imwrite(str(c_)+".jpg",frame)
        
        img_1 = cv2.imread("0.jpg")
        img = cv2.imread("Capturing.jpg", cv2.IMREAD_GRAYSCALE)
        _, threshold = cv2.threshold(img, 300, 230, cv2.THRESH_BINARY)
        _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        font=cv2.FONT_HERSHEY_COMPLEX
        
        for cnt in contours:
            cv2.drawContours(img, [cnt], 0, (0),5)
            approx=cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
            cv2.drawContours(img_1,[approx],0,(0),2)
            #print (len(approx))
            #area=cv2.contourArea(cnt)
            #print (area)
            cv2.putText(img,"yty")
            if len(approx)==3:
                print(approx.ravel())
                x=approx.ravel()[0]
                y=approx.ravel()[1]
                cv2.putText(img_1,"TRIANGEL",(x,y),font,0.5,(0))
                area=cv2.contourArea(cnt)
                
               
        
                print (area)
        cv2.imshow("0.jpg", img)
        cv2.imshow("0.jpg", img_1)
        
        
        
        
        #cv2.imwrite(str(c_))
        
