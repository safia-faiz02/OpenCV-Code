from abc import ABC
import cv2 as cv
img = cv.imread('Photos/flower.jpg')
cv.imshow('Flower',img)
cv.waitKey(0)

#Part (a)
# Resize the image
resized = cv.resize(img, (512,512),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)
cv.waitKey(0)

#Part (b)
#Converting the resized image to grayscale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
cv.waitKey(0)

#Part (c)
#Binarizing the grayscaled image
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
#looks at the img compares each pixel value to this threshold value
#if it above 150 it sets it to 255
cv.imshow('Simple Thresholded',thresh)
cv.waitKey(0)

#Part (d)
# Apply gradient filter on the original image
sobelx = cv.Sobel(resized,cv.CV_64F,1,0)
sobely = cv.Sobel(resized,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_and(sobelx,sobely)
cv.imshow('Combined Sobel',combined_sobel)
cv.waitKey(0)