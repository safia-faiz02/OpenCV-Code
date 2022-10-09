import cv2 as cv   #import statement

#READING IMAGES

# img = cv.imread('Photos/cat.jpg')   #reading the image desired
#if you give a wrong path, the program will raise an error
# cv.imshow('Cat', img)  #display image in new window

# cv.waitKey(0)   #to wait a specific amount of time (0==infinite/which is supposed to be taken)

#READING VIDEOS
capture = cv.VideoCapture('Video/cat.mp4')  #(0) == using the webcam default, 1==using first cam installed etc.
 #capture variable is an instance of VideoCapture class
while True:  #we grab the video frame by frame
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)  #display each frame by using this
    #the program when runs out of frames breaks itself and raises an error
    if cv.waitKey(20) & 0xFF==ord('d'):
        break  #it says if the letter D is pressed then break out of the loop and stop displaying the video

capture.release()
cv.destroyAllWindows()






