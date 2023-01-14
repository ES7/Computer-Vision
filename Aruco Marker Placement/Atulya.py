import numpy as np 
import cv2
import cv2.aruco as aruco
import imutils
import math

#MAIN
a1 = cv2.imread('1.jpg')
a2 = cv2.imread('2.jpg')
a3 = cv2.imread('3.jpg')
a4 = cv2.imread('4.jpg')

la = [a1,a2,a3,a4]
lid = []

img = cv2.imread('CVTask.png') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
_, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

def findArucoMarkers(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_5X5_250')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    corners, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters=arucoParam)
    return (corners, ids, rejected)

for i in la:
    a=(findArucoMarkers(i))
    lid.append(a[1][0][0])
    
def arucocoordinates(img):
    (c,i,r) = findArucoMarkers(img)
    if len(c)> 0:
        i = i.flatten()
        for (markercorner,markerid) in zip(c,i):
            corner = markercorner.reshape((4,2))
            (tl,tr,br,bl) = corner
            tl = (int(tl[0]),int(tl[1]))
            tr = (int(tr[0]),int(tr[1]))
            bl = (int(bl[0]),int(bl[1]))
            br = (int(br[0]),int(br[1]))
        return tl,tr,br,bl

def cropimg(img):
    tl,tr,br,bl = arucocoordinates(img)
    ci = img[tl[0]:br[0], tl[1]:br[1]]
    return ci

def fixaruco(img):
    tl, tr, br, bl = arucocoordinates(img)
    m = (tl[1] - tr[1])/(tl[0] - tr[0])
    theta = math.degrees(math.atan(m))
    rimg = imutils.rotate_bound(img, -theta)
    cimg = cropimg(rimg)
    return cimg

def findColor(value):
    if ((value[0]==0) and (value[1]==0) and (value[2]==0)):
        return 3
    if ((value[0]==210) and (value[1]==222) and (value[2]==228)):
        return 4
    if ((value[0]==9) and (value[1]==127) and (value[2]==239)):
        return 2
    if ((value[0]==79) and (value[1]==209) and (value[2]==146)):
        return 1
    else:
        return none




for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    #print(approx)
    
    #cv2.drawContours(img, [approx], 0, (0,0,0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    n = approx.ravel()
    i = 0

    if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h

        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            
            angle = math.degrees(math.atan((approx[2][0][1]-approx[1][0][1])/(approx[2][0][0]-approx[1][0][0])))
            
            dx = int(math.sqrt(((approx[0][0][1]-approx[1][0][1])**2)+((approx[0][0][0]-approx[1][0][0])**2)))
            dy = int(math.sqrt(((approx[2][0][1]-approx[1][0][1])**2)+((approx[2][0][0]-approx[1][0][0])**2)))

            
            if findColor(img[int(y+(h/2)), int(x+(w/2))])==1:
                cv2.drawContours(img,[contour],0,(0,0,0),-1)
                aru = cv2.resize(fixaruco(cv2.imread('1.jpg')),(dx,dy))
                aru = imutils.rotate_bound(aru,angle+90)
                img[y:y+h-2,x:x+w-2] = img[y:y+h-2,x:x+w-2]+aru      
            
            elif findColor(img[int(y+(h/2)), int(x+(w/2))])==2:
                cv2.drawContours(img,[contour],0,(0,0,0),-1)
                aru = cv2.resize(fixaruco(cv2.imread('2.jpg')),(dx,dy))
                aru = imutils.rotate_bound(aru,angle-90)
                img[y:y+h-2,x:x+w-2] = img[y:y+h-2,x:x+w-2]+aru

            elif findColor(img[int(y+(h/2)), int(x+(w/2))])==3:
                cv2.drawContours(img,[contour],0,(0,0,0),-1)
                aru = cv2.resize(fixaruco(cv2.imread('3.jpg')),(dx,dy))
                aru = imutils.rotate_bound(aru,angle+90)
                img[y:y+h-1,x:x+w-3] = img[y:y+h-1,x:x+w-3] + aru

            elif findColor(img[int(y+(h/2)), int(x+(w/2))])==4:
                cv2.drawContours(img,[contour],0,(0,0,0),-1)
                aru = cv2.resize(fixaruco(cv2.imread('4.jpg')),(dx,dy))
                aru = imutils.rotate_bound(aru,angle+90)
                img[y:y+h-2,x:x+w-2] = img[y:y+h-2,x:x+w-2]+ aru
            else:
                pass
            

            cv2.imshow("bimg",img)
            
            
cv2.imwrite("final.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
