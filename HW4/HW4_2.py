import cv2
import numpy as np

banner=cv2.imread('2-2.jpg')
copy= np.array(banner)
frame=cv2.imread('2-3.jpg')
img2=cv2.imread('2-1.jpg')

banner_corners=[[2065,1417],[1304,1416],[1969,864],[1246,1047]]
for p in banner_corners:
    cv2.circle(copy,tuple(p), 10, (0,255,0))
copy=cv2.pyrDown(copy)
cv2.imshow('corner of banner',copy)
cv2.imshow('frame',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
