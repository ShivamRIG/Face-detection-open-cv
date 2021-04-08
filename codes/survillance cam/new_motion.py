import cv2 as cv
import numpy as np
import time
from emailauto import *

capture =cv.VideoCapture(0)
fgbg=cv.createBackgroundSubtractorMOG2(300,400,True)

framecount=0

while(1):
    ret,frame= capture.read()

    if not ret:
        break
    
    framecount+=1
    resizedframe=cv.resize(frame,(0,0),fx=1,fy=1)

    fgmask=fgbg.apply(resizedframe)
    count=np.count_nonzero(fgmask)
    cv.imshow('frame',resizedframe)
    cv.imshow('Mask',fgmask)
    print('Frame: %d, Pixel Count: %d '%(framecount,count))
    Flage=True
    if(framecount > 1 and count > 6000):
            print('someones is out side of ur home')
            cv.putText(resizedframe,'someones is out side of ur home',(0,50),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA)
            

            filename='alert_intruder.jpg'
            if Flage==True:
                cv.imwrite(filename,resizedframe)
                email_send(filename)
                Flage=False
                break

            

    k = cv.waitKey(1)
    if k==ord('q'):
        break
capture.release()
cv.destroyAllWindows()