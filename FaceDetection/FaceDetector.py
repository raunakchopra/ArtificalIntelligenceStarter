import cv2
import random

trainedFaceData = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img = cv2.imread('friends.jpg') #img reading fucntion

# grayScaledImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #Turning Image to grayscale

webcam = cv2.VideoCapture(0)

while True:
    ret,frame = webcam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceCoordinates = trainedFaceData.detectMultiScale(gray)
    for (x,y,w,h) in faceCoordinates: #looping through number of faces detected 
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

    if key == 81 or key==113:
        break
webcam.release()


# faceCoordinates = trainedFaceData.detectMultiScale(grayScaledImg)

# for (x,y,w,h) in faceCoordinates: #looping through number of faces detected 
#     cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)
    
# cv2.imshow('AI APP', img) #opens a new window to display image
# cv2.waitKey() #pauses the code execution 