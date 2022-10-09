#rescaling a video refers to modifying hieght width etc
#best practice is to downscale or change the width and height
import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame, scale=0.75):
    '''This will work for imgs, vids and live vids'''
    width = int(frame.shape[1] * scale)  #width of your frame/image
    height = int(frame.shape[0] * scale)  #height of the img
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('Image',resized_image)

def changeRes(width,height):
    '''only works for live video'''
    capture.set(3,width)
    capture.set(4,height)

#READING VIDEOS
capture = cv.VideoCapture('Video/cat.mp4')  #(0) == using the webcam default, 1==using first cam installed etc.
 #capture variable is an instance of VideoCapture class
while True:  #we grab the video frame by frame
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=.2)
    # cv.imshow('Video',frame)  #display each frame by using this
    # cv.imshow('Video Resized', frame_resized)
    #the program when runs out of frames breaks itself and raises an error
    if cv.waitKey(20) & 0xFF==ord('d'):
        break  #it says if the letter D is pressed then break out of the loop and stop displaying the video

capture.release()
cv.destroyAllWindows()