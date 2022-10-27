import cv2 as cv

img=cv.imread('/home/python_learing/openCV/mm.jpg')

cv.imshow('input image',img)

cv.waitKey(0)
cv.destoryAllWindows()