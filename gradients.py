import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# canny edge detector == advanced edge detection algo
#laplacian
#computes the gradients of this grayscale img 
#imgs cannot itself have negative pixel values
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))   #compute the absolute value of the img because there can be negative but negative values can't be considered as a pixel value
cv.imshow('Laplacian',lap)

#Sobel
#computes gradients in 2 directions, x and y
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_and(sobelx,sobely)
cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Combined Sobel',combined_sobel)

canny = cv.Canny(gray,150,175)
cv.imshow('Canny',canny)
cv.waitKey(0)