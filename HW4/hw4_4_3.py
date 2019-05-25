import cv2
import numpy as np 

F=np.load('fundM.npy')
im1=cv2.imread('4-3.jpg')
im2=cv2.imread('4-4.jpg')
copy=np.array(im1)  

pt=np.array([[[268,308]]])
line = cv2.computeCorrespondEpilines(pt,2,F)
line = np.squeeze(line)
#(c,y0) , (0,y1)
y0=int(-(line[2]+im1.shape[1]*line[0])/line[1])
y1=int(-line[2]/line[1])
cv2.line(copy,(im1.shape[1],y0),(0,y1),(0,0,255))
cv2.imshow('epiline of point',copy)
cv2.waitKey()
cv2.destroyAllWindows()



 

