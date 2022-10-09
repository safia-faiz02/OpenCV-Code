import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
#dimensions of the mask should be of the same isze of that of an img or else its not going to work
cv.imshow('Blank Image',blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2+ 45,img.shape[0]//2),100,255,-1)
# cv.imshow('Mask',circle)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird shape',weird_shape)
#masking can be done with the help of bitwise ops
#allows us to focus parts of an img
#high lvl intuition behind this

masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shape Masked Image',masked)

cv.waitKey(0)