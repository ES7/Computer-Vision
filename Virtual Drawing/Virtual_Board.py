import cv2 as cv
import numpy as np
import time
import os
import htm

cTime = 0
pTime = 0
tipID = [4,8,12,16,28]

folderPath = 'Header'
myList = os.listdir(folderPath)
print(myList)
overLayList = []

for imgPath in myList:
    img = cv.imread(f'{folderPath}/{imgPath}')
    overLayList.append(img)
print(len(overLayList))

header = overLayList[0]
# header = header[:, :900]
drawColor = (255,0,255)
brushThickness = 15
eraserThickness = 100


cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 125)
xp,yp = 0,0
imgCanvas = np.zeros((720,1280,3),np.uint8)
detector = htm.handDetector()

while True:
    _, img = cap.read()
    img = cv.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # print(lmList)
        
        #Tip of inder & middle fingers
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]
        fingers = detector.fingersUp()
        # print(fingers)

        #Selecting Tools from header
        if fingers[1] and [2] :
            xp,yp = 0,0
            # print("Selection Mode")
            if y1 < 125:
                #Checking for the click
                if 20<x1<100:
                    header = overLayList[0]
                    drawColor = (51,85,253)
                elif 200<x1<250:
                    header = overLayList[1]
                    drawColor = (254,16,254)
                elif 300<x1<400:
                    header = overLayList[2]
                    drawColor = (246,81,0)
                elif 430<x1<480:
                    header = overLayList[3]
                    drawColor = (2,252,253)
                elif 520<x1<570:
                    header = overLayList[4]
                    drawColor = (0,156,25)
                elif 610<x1<700:
                    header = overLayList[5]
                    drawColor = (13,117,239)
                elif 750<x1<900:
                    header = overLayList[6]
                    drawColor = (0,0,0)

            if lmList[tipID[2]][1] < lmList[tipID[2]-1][1]:
                cv.rectangle(img, (x1,y1-30), (x2,y2+30), drawColor, cv.FILLED)

        if fingers[1] and fingers[2] == False:
            cv.circle(img, (x1,y1), 20, drawColor, cv.FILLED)
            # print("Drawing Mode")

            if xp==0 and yp==0:
                xp,yp = x1,y1

            if drawColor == (0,0,0):
                cv.line(img, (xp,yp), (x1,y1), drawColor, eraserThickness)
                cv.line(imgCanvas, (xp,yp), (x1,y1), drawColor, eraserThickness)
            else:
                cv.line(img, (xp,yp), (x1,y1), drawColor, brushThickness)
                cv.line(imgCanvas, (xp,yp), (x1,y1), drawColor, brushThickness)
            xp,yp = x1,y1

    imgGray = cv.cvtColor(imgCanvas, cv.COLOR_BGR2GRAY)
    _, imgInv = cv.threshold(imgGray, 50,255, cv.THRESH_BINARY_INV)
    imgInv = cv.cvtColor(imgInv, cv.COLOR_GRAY2BGR)
    img = cv.bitwise_and(img, imgInv)
    img = cv.bitwise_or(img, imgCanvas)

    img[0:125,0:1280] = header
    #Blending both the images
    # img = cv.addWeighted(img,0.5,imgCanvas,0.5,0)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img, f'FPS : {str(int(fps))}', (1030,78), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)

    cv.imshow("Image",img)
    if cv.waitKey(5) & 0xFF == ord('q'):
        break