#coding:utf-8

import cv2
import sys

#顔探索用のカスケード型分類器を取得
#haarcascade_frontalface_default.xmlのパスを渡す 
face_cascade = cv2.CascadeClassifier("/home/pi/install/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml")

file = sys.argv[1]

img = cv2.imread(file)

#読み込んだ画像をグレースケールに変換
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#分類器で顔を認識する
face = face_cascade.detectMultiScale(gray,1.3,5)

if 0 < len(face):

    print "get face"

    for (x,y,w,h) in face:
	#the input to cv.HaarDetectObjects was resized, scale the
      	#bounding box of each face and convert it to two CvPoints 
      	pt1 = (int(x), int(y))
      	pt2 = (int((x + w)), int((y + h)))
      	cv2.rectangle(img, pt1, pt2, (255, 0, 0), 3, 8, 0)
    cv2.imwrite("detectedface.jpg",img)
else:

    print "no face"
