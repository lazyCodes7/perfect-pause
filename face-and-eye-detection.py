import numpy as np 
import cv2 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml') 

first_read = True

cap = cv2.VideoCapture(0) 
ret,img = cap.read() 

while(ret): 
    ret,img = cap.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray = cv2.bilateralFilter(gray,5,1,1) 

    faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(200,200)) 
    if(len(faces)>0): 
        for (x,y,w,h) in faces: 
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),10) 

            roi_face = gray[y:y+h,x:x+w] 
            roi_face_clr = img[y:y+h,x:x+w] 
            eyes = eye_cascade.detectMultiScale(img,1.3,5,minSize=(50,50)) 
            for (ex,ey,ew,eh) in eyes: 
                img=cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,0,255),2) 
            
            if(len(eyes)>=2): 
                
                    cv2.putText(img, 
                    "Play video", (70,70), 
                    cv2.FONT_HERSHEY_PLAIN, 3, 
                    (0,255,0),2) 
            else: 
                if(first_read): 
                    cv2.putText(img, 
                    "Pause Video - eyes closed", (70,70), 
                    cv2.FONT_HERSHEY_PLAIN, 2, 
                    (0,255,255),3) 
            
    else: 
        cv2.putText(img, 
        "Pause video - user looking away",(70,70), 
        cv2.FONT_HERSHEY_PLAIN, 2, 
        (0,0,255),2) 

    #Controlling the algorithm with keys 
    cv2.imshow('img',img) 
    a = cv2.waitKey(1) 
    if(a==ord('q')): 
        break
    elif(a==ord('s') and first_read): 
        #This will start the detection 
        first_read = False

cap.release() 
cv2.destroyAllWindows() 
