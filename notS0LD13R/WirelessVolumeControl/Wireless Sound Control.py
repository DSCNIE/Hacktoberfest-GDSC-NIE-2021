import cv2
import mediapipe as mp
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#Pycaw Black Magic
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

'''''
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-20.0, None)
'''''

mpDraws=mp.solutions.drawing_utils
mpHands=mp.solutions.hands
hands=mpHands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.8)

minVol,maxVol=volume.GetVolumeRange()[:2]

cap=cv2.VideoCapture(0)
print("Press Esc to close the window")
while True:
    success,img=cap.read()
    
    results=hands.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks: 
        for handLms in results.multi_hand_landmarks:#results.multi_hand_landmarks=[20 x landmark{x: y: z:}]
            lmList=[]
            for id,lm in enumerate(handLms.landmark):#id=1 to 20 lm.x=x lm.y=y lm.z=z
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
            if lmList:#lmList is list of 20 list containing id x and y
                x1,y1=lmList[4][1],lmList[4][2]    
                x2,y2=lmList[8][1],lmList[8][2] 
                length=math.hypot(x2-x1,y2-y1)   
                
                #adjusting volume to fit weird range of getvolumerange()
                vol=np.interp(length,[50,250],[minVol,maxVol])   
                volume.SetMasterVolumeLevel(vol, None) 
                percentage=100-(vol*100//minVol)
                
                
                #drawing dots and lines
                if length>=50:
                    clr=(percentage,percentage,2.55*percentage)#dynamic color
                    cv2.line(img,(x1,y1),(x2,y2),clr,3)
                    cv2.circle(img,(x1,y1),10,(0,255,0),cv2.FILLED)
                    cv2.circle(img,(x2,y2),10,(0,255,0),cv2.FILLED)
                else:cv2.circle(img,((x2+x1)//2,(y2+y1)//2),10,(0,0,255),cv2.FILLED) 
                cv2.putText(img,'Volume='+str(percentage),(25,25),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),1)   #volume indicator    
                

    cv2.imshow('Image',img)
    if cv2.waitKey(1)==27:exit()    

  


    
