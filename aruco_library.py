#!/usr/bin/env python3
############## Task1.1 - ArUco Detection ##############

import numpy as np
import cv2
import cv2.aruco as aruco
import sys
import math
import time

def detect_ArUco(img):
    Detected_ArUco_markers = {}
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    parameters = aruco.DetectorParameters_create()
    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    for i in range(0, len(ids)):
        Detected_ArUco_markers[ids[i][0]] = corners[i][0]
    return Detected_ArUco_markers

def Calculate_orientation_in_degree(Detected_ArUco_markers):
    ArUco_marker_angles = {}
    for id in Detected_ArUco_markers:
        green_x = Detected_ArUco_markers[id][1][0];green_y = Detected_ArUco_markers[id][1][1]
        grey_x = Detected_ArUco_markers[id][0][0];grey_y = Detected_ArUco_markers[id][0][1]
        pink_x = Detected_ArUco_markers[id][2][0];pink_y = Detected_ArUco_markers[id][2][1]
        white_x = Detected_ArUco_markers[id][3][0];white_y = Detected_ArUco_markers[id][3][1]
        angle = round(math.degrees(math.atan2((white_y-grey_y),(grey_x-white_x))))
        angle = angle if angle>=0 else 360+angle
        ArUco_marker_angles[id] = angle
    return ArUco_marker_angles

def mark_ArUco(img,Detected_ArUco_markers,ArUco_marker_angles):
    for id in Detected_ArUco_markers:
        green_x = Detected_ArUco_markers[id][1][0];green_y = Detected_ArUco_markers[id][1][1]
        grey_x = Detected_ArUco_markers[id][0][0];grey_y = Detected_ArUco_markers[id][0][1]
        pink_x = Detected_ArUco_markers[id][2][0];pink_y = Detected_ArUco_markers[id][2][1]
        white_x = Detected_ArUco_markers[id][3][0];white_y = Detected_ArUco_markers[id][3][1]
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
        #cv2.line(img,(int(x_center)+25,0),(int(x_center)+25,400),(255,0,0),2)
        #cv2.line(img,(int(x_center)-25,0),(int(x_center)-25,400),(255,0,0),2)
        cv2.putText(img,f"{id}",(int(green_x+10),int(green_y)+10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
        angle = ArUco_marker_angles[id]
        cv2.putText(img,f"{angle}",(int(white_x)-20,int(white_y)-20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
    return img
