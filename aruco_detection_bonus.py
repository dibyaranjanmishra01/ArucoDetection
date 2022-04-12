import numpy as np
import cv2
import cv2.aruco as ar
import math

def doprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    aruco_dict = ar.Dictionary_get(ar.DICT_5X5_250)
    parameters = ar.DetectorParameters_create()
    corners, ids, _ = ar.detectMarkers(gray, aruco_dict, parameters=parameters)
    if ids is not None :
        dict = {}

        for i in range(0, len(ids)):
            dict[ids[i][0]] = corners[i][0]

        for id in dict:
            green_x = dict[id][1][0];green_y = dict[id][1][1]
            grey_x = dict[id][0][0];grey_y = dict[id][0][1]
            pink_x = dict[id][2][0];pink_y = dict[id][2][1]
            white_x = dict[id][3][0];white_y = dict[id][3][1]
            cv2.circle(img,(green_x,green_y),5,(0,256,0),-1)
            cv2.circle(img,(grey_x,grey_y),5,(125,125,125),-1)
            cv2.circle(img,(pink_x,pink_y),5,(180,105,255),-1)
            cv2.circle(img,(white_x,white_y),5,(255,255,255),-1)
            x_center = ((grey_x+pink_x)/2+(white_x+green_x)/2)/2
            y_center = ((grey_y+pink_y)/2+(white_y+green_y)/2)/2
            cv2.circle(img,(int(x_center),int(y_center)),5,(0,0,255),-1)
            x_mid = (grey_x+green_x)/2
            y_mid = (grey_y+green_y)/2
            cv2.line(img,(int(x_center),int(y_center)),(int(x_mid),int(y_mid)),(255,0,0),5)
            cv2.putText(img,f"{id}",(int(green_x+10),int(green_y)+10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
            angle = round(math.degrees(math.atan2((white_y-grey_y),(grey_x-white_x))))
            angle = angle if angle>=0 else 360+angle
            #print(x_mid,",",y_mid,"  ",x_center,",",y_center)
            cv2.putText(img,f"{angle}",(int(white_x)-20,int(white_y)-20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
    return img



cap = cv2.VideoCapture("VIDEO.mp4")
result = cv2.VideoWriter('RESULT_VIDEO.avi',cv2.VideoWriter_fourcc(*'MJPG'),20,(int(cap.get(3)),int(cap.get(4))))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        image = doprocess(frame)
        cv2.imshow('Frame',image)
        result.write(image)
        if(cv2.waitKey(25)&0xFF == ord("q")):
            break
    else:
        break

cap.release()
result.release()
cv2.destroyAllWindows()