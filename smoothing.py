import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

#most preferred method to blur == Gaussian Blur

# we draw a window on a specific portion of a given image
#window has a size,kernel size, no of rows and columns (r,c)
#something happens in the surrounded pixel due to surrounding pixels


# Averaging
# we define a window, this window will essentially compute the pixel intensity of the mid pixel of the true center as the average of the surrounding pixel intensities
#this process happens everywhere in the image
#when it gets done in left, then it moves to right then down and compute the ang of the all the pizels in the img

average = cv.blur(img, (3,3))
cv.imshow('Average Blur',average)

#Gaussian Blur
#does the same thing as averaging
#instead of computing the avg of all the surrounding pixel intensity, eahc surrounding pixel is given a particular wieght, and essentially the ang of the products of those weights give u the value for the true center
# compared to averaging u get less blurring
#more natural as compared to averaging

gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur
#same thing as averaging except that it finds median instead of average of the pixel intensity
#more effective when it comes to noise in the img compared to both
#used to remove salt and pepper noise 
#used in advanced C.V projects that tend to depend on the reduction of the substantial amount of noise
#not meant for high kernel sizes like 7 or even 5 in some cases
#more ffective in reducing some of the noise in the img

median = cv.medianBlur(img, 3)  #it automatically assumes itself as (3,3)
cv.imshow('Median Blur',median)

#Bilateral Blurring
#the most effective, used in most advance C.V projects, essentially because of how it blurs
#traditionally it blurs the image without looking at the edges in the img or not
#applies blurring but redeems the edges in the img
#we a pass a diameter not a kernel size
#color sigma == more color in the neighbourhood that will be considered during the blur
# sigma space == larger values of the space means pixels further out from the central pixel will influence the blurring technique  
#in sigma space you're essentially indicating that from what area should the blurring be done what should be affecting the blurring in the center
#washed out,smudged looking picture after given a huge value similar to median blur

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur',bilateral)

cv.waitKey(0)