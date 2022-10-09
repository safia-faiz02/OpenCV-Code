import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(gray, (5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges',canny)

# ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('Threshold',thresh)
#coverts the img to zero/black or white/one


# useful in shape analysis and object detection and recognition
contours , hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# findContours method looks at the canny img and then examines it
#RETR_LIST == all the coordinates found in the contour img,returns all the contours find in the img
#CHAIN_APPROX_NONE == refers to hierarchical representation of the contours
#RETR_EXTERNAL == finds all the external contours
#RETR_TREE == returns all the hierarchical contours 
#CHAIN_APPROX == contour approximation method, how we want to approximate the contour
#CHAIN_APPROX_NONE == does nothing, return everything, all the contours all the coordinates of the points
#CHAIN_APPROX_SIMPLE == it essentially compresses all the quantities that are returned
print(f'{len(contours)} contour(s) are found')
cv.drawContours(blank, contours, -1, (0,0,255), 1)  #takes an img to draw over, takes a contour/list, takes a contour index, takes, color, thickness
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)

#recommended == use scanning method first and then try to find the contours rather than try to threshold the image and then find the contours on that.