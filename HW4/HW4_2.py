import cv2
import numpy as np

banner=cv2.imread('2-2.jpg')
copy= np.array(banner)
frame=cv2.imread('2-3.jpg')
frame2=cv2.imread('2-1.jpg')

banner_corners=np.array([[1246,1047],[1969,864],[2065,1417],[1304,1416]])
for i,p in enumerate(banner_corners):
    cv2.circle(copy,tuple(p), i*2+1, (0,255,0),3)
copy=cv2.pyrDown(copy)
copy=cv2.pyrDown(copy)
#cv2.imshow('corner of banner',copy)

frame_corners=np.array([[0,0],[frame.shape[0],0],[frame.shape[0],frame.shape[1]],[0,frame.shape[1]]])
M = cv2.GetPerspectiveTransform(frame_corners,banner_corners)
dst=cv2.warpPerspective(frame,M,dsize=(banner.shape[1],banner.shape[0]))

mask = cv2.warpPerspective(np.ones(frame.shape)*255,M,dsize=(banner.shape[1],banner.shape[0]))

#res=cv2.bitwise_or(mask,banner)
copy=cv2.pyrDown(mask)
copy=cv2.pyrDown(copy)

cv2.imshow('warped',copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
