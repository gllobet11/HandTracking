import cv2
import time
import mediapipe as mp

cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands(False)
mpDraw=mp.solutions.drawing_utils
#static_image_mode=False == detecs if not can switch between detects and track
pTime=0
cTime=0

while True:
    succes, img=cap.read()
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hands_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm)#The location should be in pixels we need to convert
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy) #how do we know which landmark is it? we need to print id
                #if id==4:
                cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
    (255,0,255),3)

    cv2.imshow('Image',img)
    cv2.waitKey(1)