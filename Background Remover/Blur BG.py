import cv2 as cv
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()
imgBG = cv.imread("Images/download.jfif")

listImg = os.listdir("Images")
print(listImg)
imgList = []
for imgPath in listImg:
    img = cv.imread(f'Images/{imgPath}')
    imgList.append(img)
print(len(imgPath))

indexImg = 0

while True:
    success, img = cap.read()
    blurImg = cv.blur(img,(40,40)) 
    imgOut = segmentor.removeBG(img, blurImg, threshold=0.7)
    

    imgStacked = cvzone.stackImages([img,imgOut],2,1)
    _, imgStacked = fpsReader.update(imgStacked, color=(0,0,255))

    print(indexImg)
    cv.imshow("Image",imgStacked)
    key = cv.waitKey(1)
    if key == ord('a'):
        if indexImg>0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList)-1 :
            indexImg += 1
    elif key == ord('q'):
        break