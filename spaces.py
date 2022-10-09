import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)


#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR To HSV
hsv =cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR To L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#BGR TP RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV To BGR',hsv_bgr)

#LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB To BGR',lab_bgr)

plt.imshow(rgb)  #matplotlib shows the reversed BGR colors (rgb)
#to let it show in RGB, you've to convert the image first from bgr to rgb and then pass it as an arg to the plt
plt.show()

cv.waitKey(0)

#you can't convert grayscale to hsv directly, if you want to do that, you first have to convert it into bgr 