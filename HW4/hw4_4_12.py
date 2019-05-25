import cv2
import numpy as np 

#________________________________________________________________________
im1=cv2.imread('4-1.jpg')
im2=cv2.imread('4-2.jpg')
copy=np.array(im1)

found,corners11=cv2.findChessboardCorners(im1,(7,8))
found,corners12=cv2.findChessboardCorners(im1,(6,5))

corners11=np.squeeze(corners11)
corners12=np.squeeze(corners12)
corners1=np.vstack((corners11,corners12))

found,corners21=cv2.findChessboardCorners(im2,(7,8))
found,corners22=cv2.findChessboardCorners(im2,(6,5))

corners21=np.squeeze(corners21)
corners22=np.squeeze(corners22)
corners2=np.vstack((corners21,corners22))


for p in corners1:
    cv2.circle(copy,tuple(p), 3, (0,255,0))
cv2.imshow('chess board corners',copy)
cv2.waitKey()
cv2.destroyAllWindows()

#___________________________________________________________
F,mask=cv2.findFundamentalMat(corners1,corners2)
print(F)
np.save('fundM',F)
