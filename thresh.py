import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

#thresholding is a binarilaztion of an image
#to take an img and convert it into binary image
# 0 == black, 255 == white
#to take a thresholding value and compare each pixel of the image to this threshold img
# if that pixel intensity < threshold value, we set that pixel intensity to zero
# if it is above the threshold value, we set it to 255/white

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
#looks at the img compares each pixel value to this threshold value
#if it above 150 it sets it to 255
#returns two things:
#thresh == binarized image
#threshold == the same value that you've passed as thresholded value
cv.imshow('Simple Thresholded',thresh)

threshold, thresh_inv= cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse',thresh_inv)
#inverse logic is applied here, if it is <150 then it will set it to 255 and vice verse

#adaptive Threshold
#downside: to manually specify a specific threshold value 
#in more advanced cases it won't work
# to let the computer find the optimal threshold value by itself
#using that value that refines, it binarizes the img

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)
#ADAPTIVE_THRESH_MEAN_C == using the neighbourhood's pixels for the minimal result
#Threshold type == THRESH_BINARY
#block size == essentially the neighbourhood size of the kernel size which opencv needs to compute mean to find the optimal threshold value
# C value == integer subtracted from the mean, the more u subtract the more accurate it is
# diff between gaussian and mean == essentially add a weight to each pixel and computed the mean across those pixels
cv.imshow('Adaptive Thresholding',adaptive_thresh)


cv.waitKey(0)