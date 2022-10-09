import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#a color image basically consists of multiple channels R G B
#take the img, and split in into three color channels

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])  #could be height and width not necessarily color channels
green = cv.merge([blank,g,blank])  #we've set the two other channels as black/blank
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)
#the o/p of these is a grayscale img as it represents 1,0

print(img.shape)
print(b.shape)  #(1500,1000, 1) not shown but it is understood that the shape of the component is 1
print(r.shape)
print(g.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged',merged)

cv.waitKey(0)