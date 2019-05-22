import cv2
import numpy as np
#___________________________________________
#change the comments to see other image warp
#___________________________________________


img=cv2.imread('1-2.jpg')
corners=np.array([[639,1034],[1212,946],[1434,1212],[686,1363]])

#img=cv2.imread('1-1.jpg')
#corners=np.array([[1111,900],[1795,1017],[1788,1405],[818,1197]])

#___________________________________________
copy=np.array(img)
for p in corners:
    cv2.circle(copy,tuple(p), 10, (0,0,255),2)

mean=np.mean(corners,0)
a=(np.linalg.norm(corners-mean))/4
newframe=np.array([mean+[-a,-a],mean+[a,-a],mean+[a,a],mean+[-a,a]]).astype(np.int)

print(newframe)
for p in newframe:
    cv2.circle(copy,tuple(p), 10, (0,0,255),2)
keypoints=cv2.pyrDown(copy)
keypoints=cv2.pyrDown(keypoints)
cv2.imshow('8 mosaic',keypoints)


M, mask = cv2.findHomography(corners, newframe, cv2.RANSAC,5.0)
dst=cv2.warpPerspective(img,M,dsize=tuple(img.shape[:2]))
show=cv2.pyrDown(dst)
show=cv2.pyrDown(show)
cv2.imshow('warped',show)
cv2.waitKey(0)
cv2.destroyAllWindows()
