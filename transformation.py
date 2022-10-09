import cv2 as cv
import numpy as np 

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat',img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> shift to left
# -y --> shift to up
# x --> shift to right
# y --> shift to down

translated = translate(img, -100, 100)
cv.imshow('translated',translated)
cv.waitKey(0)

#Rotation 
def rotate(img, angle, rotPoint=None):
    (height,width)= img. shape[:2]

    if rotPoint is None:
        rotPoint = (width//1,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated',rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Double rotate',rotated_rotated)
cv.waitKey(0)

#Resizing
resized = cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)
cv.waitKey(0)

#Flipping
flip = cv.flip(img, -1)  # 0 == flipping the img vertically/ over x axis
# 1 == flipping the img horizontally or over the y axis
# -1 == flipping it both vertically and horizontally
cv.imshow('Flip',flip)
cv.waitKey(0)

#Cropping
cropped = img[200:400,300:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)
