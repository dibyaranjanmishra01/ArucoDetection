import numpy as np
import cv2
import cv2.aruco as aruco
import time
from aruco_library import *

image_list = ["test_image1.png","test_image2.png","frame0002.jpg"]
test_num = 1

for image in image_list:
    img = cv2.imread(image)
    Detected_ArUco_markers = detect_ArUco(img)	
    angle = Calculate_orientation_in_degree(Detected_ArUco_markers)
    img = mark_ArUco(img,Detected_ArUco_markers,angle)
    result_image = "../result_image"+str(test_num)+".png"
    cv2.imwrite(result_image,img)
    test_num = test_num +1
