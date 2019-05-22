import cv2
import numpy as np

img=cv2.imread('1-2.jpg')
corners=[[1111,900],[1795,1017],[1788,1405],[818,1197]]

#img=cv2.imread('1-1.jpg')
#corners=[[1111,900],[1795,1017],[1788,1405],[818,1197]]

copy=np.array(img)
for p in corners:
    cv2.circle(copy,tuple(p), 10, (0,0,255),2)
    


corners=np.array(corners)
mean=np.mean(corners,0)
a=(np.linalg.norm(corners-mean))/4
newframe=np.array([mean+[-a,-a],mean+[a,-a],mean+[a,a],mean+[-a,a]]).astype(np.int)

for p in newframe:
    cv2.circle(copy,tuple(p), 10, (0,0,255),2)
keypoints=cv2.pyrDown(copy)
cv2.imshow('8 mosaic',keypoints)


M, mask = cv2.findHomography(corners, newframe, cv2.RANSAC,5.0)
dst=cv2.warpPerspective(img,M,dsize=tuple(img.shape[:2]))
show=cv2.pyrDown(dst)
cv2.imshow('warped',show)
cv2.waitKey(0)
cv2.destroyAllWindows()








