import cv2 as cv
import mediapipe as mp
import time

class handDetector():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=False,max_num_hands=2,min_detection_confidence=0.8,min_tracking_confidence=0.5)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipID = [4,8,12,16,28]

    def findHands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self,img,handNo=0,draw=True):
        self.lmList=[]
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                    h,w,c = img.shape
                    cx,cy = int(lm.x*w), int(lm.y*h)
                    self.lmList.append([id, cx, cy])
                    if draw:
                        cv.circle(img, (cx,cy), 10, (255,0,255), cv.FILLED)
        return self.lmList
    

    def fingersUp(self):
        fingers = []
        # for thumb
        if self.lmList[self.tipID[0]][1] < self.lmList[self.tipID[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # For index finger
        if self.lmList[self.tipID[1]][1] < self.lmList[self.tipID[1]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # For middle finger
        if self.lmList[self.tipID[2]][1] < self.lmList[self.tipID[2]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # for other 4 fingers
        # for id in range(1,4):
        #     if lmList[self.tipID[id]][2] < lmList[self.tipID[id]-2][2]:
        #         fingers.append(1)
        #     else:
        #         fingers.append(0)
        return fingers

def main():
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv.putText(img, str(int(fps)), (10,78), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)

        cv.imshow("Image",img)
        if cv.waitKey(5) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()