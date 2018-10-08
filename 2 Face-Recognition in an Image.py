import cv2

face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

img = cv2.imread("face1.jpg")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces= face_cascade.detectMultiScale(gray_img, scaleFactor = 1.15, minNeighbors=5)
print(type(faces))
print(faces)

# for x,y,w,h in faces:
#     print("x:",x)
#     print("y:",y)
#     print("w:",w)
#     print("h:",h)
#     img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

x,y,w,h = faces[0]
img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow("Face",img)
cv2.waitKey(0) # 0 : Closes as soon as we press any key 
cv2.destroyAllWindows() 
