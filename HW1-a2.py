#author: mohammad
#python3.7.1 anaconda
import cv2
import numpy as np

#determine rotation angle
angle=270
#Load image
img=cv2.imread('2.jpg')
#get shape of image
rows,cols = img.shape[:2]
#rotate corners of frame to determin new frames shape
R = cv2.getRotationMatrix2D((0,0),angle,1)
corners=np.dot(np.array([[0,0],[rows,0],[0,cols],[rows,cols]]),R).astype('int32')
#get the center of the rotated frame
center1=corners[3,:2]//2
#calculate new frame's rows and cols
corners=np.transpose(corners)
print(corners)
newrows=np.max(corners[0])-np.min(corners[0]).astype('int32')
newcols=np.max(corners[1])-np.min(corners[1]).astype('int32')

#get the center we want to have for rotated frame
center2=np.array([newrows,newcols])//2

#calculate transformation vector for rotating matrix M
T=center2-center1
#print(center2,center1)
M = cv2.getRotationMatrix2D((0,0),angle,1)
M[0,2]=T[1]
M[1,2]=T[0]

#rotate with matrix M in size newrows, newcols
dst = cv2.warpAffine(img,M,(newcols,newrows))

#display
cv2.imshow('image',img)
cv2.imshow('rotated image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()