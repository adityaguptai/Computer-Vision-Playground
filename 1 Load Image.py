import cv2

img = cv2.imread("img2.jpg",1)
# 1 for color image
# 0 for grayscale image
print(img.shape)

#cv2.imshow("Image View",img)
#cv2.waitKey(0) # 0 : Closes as soon as we press any key 
#cv2.waitKey(2000)
resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Image Resize View",resized)
cv2.imshow("Image View",img)
cv2.waitKey(0) # 0 : Closes as soon as we press any key 
cv2.destroyAllWindows() 


