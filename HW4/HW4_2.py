import cv2
import numpy as np

frame=cv2.imread('2-2.jpg')
banner=cv2.imread('2-3.jpg')
frame2=cv2.imread('2-1.jpg')

copy= np.array(frame)
h,w=banner.shape[:2]

frame_corners=[[2065,1417],[1304,1416],[1969,864],[1246,1047]]
banner_corners=[[w,h],[0,h],[w,0],[0,0]]
frame2_corners=[[1745,841],[1508,779],[1748,746],[1511,672]]
mask=np.ones(banner.shape).astype(np.uint8)


c=1
for p in frame_corners:
    cv2.circle(copy,tuple(p), 3*c, (0,255,0),3)
    c=c+1
cv2.imwrite('frame corners.jpg',copy)
copy=np.array(frame2)
for p in frame2_corners:
    cv2.circle(copy,tuple(p), 3*c, (0,255,0),3)
    c=c+1
cv2.imwrite('frame2 corners.jpg',copy)

frame_corners=np.array(frame_corners)
frame2_corners=np.array(frame2_corners)
banner_corners = np.array(banner_corners)




M,idx = cv2.findHomography(banner_corners,frame_corners, cv2.RANSAC,5.0)
dst=cv2.warpPerspective(banner,M,dsize=(frame.shape[1],frame.shape[0]))
warpedmask=cv2.warpPerspective(mask,M,dsize=(frame.shape[1],frame.shape[0]))

dst=dst*warpedmask+(1-warpedmask)*frame

cv2.imwrite('virtual1.jpg',dst)

M,idx = cv2.findHomography(banner_corners,frame2_corners, cv2.RANSAC,5.0)
dst=cv2.warpPerspective(banner,M,dsize=(frame.shape[1],frame.shape[0]))
warpedmask=cv2.warpPerspective(mask,M,dsize=(frame.shape[1],frame.shape[0]))

dst=dst*warpedmask+(1-warpedmask)*frame2
cv2.imwrite('virtual2.jpg',dst)

