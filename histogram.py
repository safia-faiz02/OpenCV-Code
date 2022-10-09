import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

# gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image',masked)

#Grayscale Histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256],[0,256])
# #calcHist([no. of pics],[no. of channels which basically specify the index we want to compute a histogram for],mask, [no. of bins that we want to use for computing the histogram], ranges for all possible pixel values)
# #for grayscale img == [0]

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')  #shows the intervals of pixel intensities
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#Color Histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')  #shows the intervals of pixel intensities
plt.ylabel('# of pixels')
color = ('b','g','r')
for i,col in enumerate(color):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])


plt.show()
cv.waitKey(0)

#allows u to visualize the distribution of pixel intensity of an img