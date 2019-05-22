import cv2

img1 = cv2.imread('3-1.jpeg')
img2 = cv2.imread('3-2.jpeg')

detector = cv2.AKAZE_create()
(kps1, descs1) = detector.detectAndCompute(img1, None)
(kps2, descs2) = detector.detectAndCompute(img2, None)

# Match the features
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = bf.knnMatch(descs1,descs2, k=2)    # typo fixed

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.9*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
im3 = cv2.drawMatchesKnn(img1, kps1, img2, kps2, good[1:20], None, flags=2)
cv2.imshow("AKAZE matching", im3)
cv2.waitKey(0) 








    