import cv2
import mediapipe as mp
print(cv2.__version__)
hands=mp.solutions.hands.Hands(False,5,.5,.5)
myDraw=mp.solutions.drawing_utils
def parseLandmark(frame):
    myHands=[]
    frameBGR=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    result=hands.process(frameBGR)
    if result.multi_hand_landmarks !=None:
        for landMarks in result.multi_hand_landmarks:
            myHand=[]
            myDraw.draw_landmarks(frame,landMarks,mp.solutions.hands.HAND_CONNECTIONS)
            for landmark in landMarks.landmark:
                myHand.append((int(landmark.x*width),int(landmark.y*height)))
            myHands.append(myHand)
    return myHands
width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))

while True:
    ignore,frame=cam.read()
    myHands=parseLandmark(frame)
    for hand in myHands:
        maps=[3,7,11,15,19]
        for map in maps:
            cv2.circle(frame,hand[map],20,(0,0,255),-1)
    cv2.imshow("Windows",frame)
    cv2.moveWindow("Windows",0,0)
    if cv2.waitKey(1) & 0xff==ord("r"):
        break
cam.release()
