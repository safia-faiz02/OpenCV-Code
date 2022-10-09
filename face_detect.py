import cv2 as cv

img = cv.imread('Photos/cringemas.jpg')
cv.imshow('Cringemas',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Cringemas G',gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
#uses scaleFactor and minNeighbors to essentially detect a face and return coordinates of that face as a list to faces_rect
#can print the length of these faces 
print(f'Number of faces found = {len(faces_rect)}')
#faces_rect == rectangular coordinates for faces that are present in the img
#what we can do is essentially loop over this list and grab the coordinates of those imgs and draw a rectangle over the detected faces

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Faces',img)
cv.waitKey(0)
#haar cascades are sensitive to noise in an img
#not the most effective in detecting faces
#not what you would use in a more advanced C.V project
#deeler's face recognizer is more effective and less sensitive to noise in img
#easy to use and setup
#can extend to videos, detect haar cascades in each individual frame of a video
