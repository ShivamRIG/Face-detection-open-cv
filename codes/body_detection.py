#import-----> open cv in pyhton
import cv2 as cv
# Loding the CascadeClassifier in body varible
body = cv.CascadeClassifier("D:\\project\\web-Django\\codes\\cascadedata\\haarcascade_fullbody.xml")
#Capturing-frame---> VideoCapture function("moskva.mov") capture the frame  in cap 
cap = cv.VideoCapture("D:\\project\\web-Django\\codes\\Video\\moskva.mov")
#looping the Video--->  to get the frame
while cap.isOpened():
# reading and storing the number value 
    ret, frame =cap.read()
#resizing the video
    resize=cv.resize(frame,(640,480))
#converting it to gray
    gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
#performing the dection on the video   
    bodys=body.detectMultiScale(gray,1.1,3)
#drawing the rectangle on the video 
    for(x,y,w,h)in bodys:
        cv.rectangle(resize,(x,y),(x+w,y+h),(255,0,255),2)
#show the video  on the window     
        cv.imshow("body detection",resize)
#this is for quting the window 
    if cv.waitKey(1)&0xFF ==ord('q'):
        break

