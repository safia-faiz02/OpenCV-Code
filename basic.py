import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)
cv.waitKey(0)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
cv.waitKey(0)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
cv.waitKey(0)

#Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges',canny)
cv.waitKey(0)

#Dialating the img
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated',dilated)
cv.waitKey(0)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded',eroded)
cv.waitKey(0)

# Resize
resized = cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)
cv.waitKey(0)

# Cropping
crop = img[50:200,200:400]
cv.imshow('Cropped',crop)
cv.waitKey(0)