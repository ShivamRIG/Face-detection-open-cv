import cv2 as cv
import time
cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
video=cv.VideoCapture(0)
while True:
    check,frame=video.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=6)
    for x,y,w,h in faces:
        frame=cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow("frame",frame)
    key  = cv.waitKey(1)    
    if key==ord('q'):
        break
        
    

video.release() 
cv.destroyAllWindows()
