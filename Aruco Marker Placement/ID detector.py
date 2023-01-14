import cv2
import cv2.aruco as aruco
import numpy as np

def findArucoMarkers(img, markerSize=6, totalMarkers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_5X5_250')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    corners, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters=arucoParam)

    if len(corners) > 0:
        ids = ids.flatten()

        for (markerCounter, markerID) in zip(corners, ids):
            corners = markerCounter.reshape((4,2))
            (tl, tr, br, bl) = corners

            tr = (int(tr[0]), int(tr[1]))
            tl = (int(tl[0]), int(tl[1]))
            bl = (int(bl[0]), int(bl[1]))
            br = (int(br[0]), int(br[1]))

            cv2.putText(img, str(markerID), tl,cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)

cap = cv2.VideoCapture(0)

while True:
    check, frame = cap.read()

    if check:
        findArucoMarkers(frame)
        cv2.imshow("image", frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
