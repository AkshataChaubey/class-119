import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

tracker=cv2.TrackerCSRT_create()

print("what is tracker",tracker)

returned,myimage=video.read()

bbox=cv2.selectROI("Tracking",myimage,False)

tracker.init(myimage,bbox)

print(bbox)

def drawbox(myimage,bbox):

    #x,y,w,h
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(myimage,(x,y),((x+w),(y+h)),(255,0,0),2,1)
    cv2.putText(myimage,"Tracking",(75,90),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,2)

while True:
    check,img = video.read()   
    success,bbox=tracker.update(img)
    print("what is success")
    if success==True:
        drawbox(img,bbox)
    else:
        cv2.putText(img,"lost")    


    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



