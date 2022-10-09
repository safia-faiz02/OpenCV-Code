import cv2 as cv
from cv2 import rectangle
from cv2 import bitwise_and
import numpy as np
#AND, OR XOR and NOT
#used alot in image processing
#with working with mask
#turned off = 0, turned on = 1

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#Bitwise AND == intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise And',bitwise_and) 

#Bitwise OR == all regions inclusive
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise Or',bitwise_or) 

#Bitwise XOR
#good for returning non intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise Xor',bitwise_xor)

#Bitwise NOT
#doesn't return anything
#what it does is that inverts the binary color
bitwise_not_rect= cv.bitwise_not(rectangle)
cv.imshow('Bitwise Not Rectangle',bitwise_not_rect) 

bitwise_not_c= cv.bitwise_not(circle)
cv.imshow('Bitwise Not Circle',bitwise_not_c)

cv.waitKey(0)