import cv2

video = cv2.VideoCapture(0)

#Cascade

face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")


a = 1

while True:
    a = a + 1
    check, frame = video.read()
    print(frame)
    print(check)
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5)
    x,y,w,h = faces[0]
    img =  cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    for x,y,w,h in faces:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    # x,y,w,h = faces[0]
    # img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("Video",img)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)

video.release()
cv2.destroyAllWindows()
