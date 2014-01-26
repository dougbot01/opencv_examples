import cv2
#import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

white = (255, 255, 255)
black = (0, 0, 0)

#Use a black and white image

image = cv2.imread('bw.png')
cv2.imshow("Image", image)
cv2.moveWindow("Image", 0, 0)

# find edges using derivative in X/Y at the same time
# doesn't work well on round shapes
# side note : from black to white, derivative is +255, no problem
#             but white to black is -255, which OpenCV changes to 1
#             I fixed these using the stats.threshold method to make
#             all values > 0 to 255
edges = image[1:,1:,:] - image[:-1,:-1,:]
edges = stats.threshold(edges, threshmax=0, newval=255)
cv2.imshow("Partial Edges", edges)
cv2.moveWindow("Partial Edges", 450, 0)

# find edges using X derivate and Y derivative separately
edgesH = image[1:,:,:] - image[:-1,:,:]
edgesV = image[:,1:,:] - image[:,:-1,:]
# add the matrices together. we have to crop a row/column for it to match size
edgesA = edgesH[:,:-1,:] + edgesV[:-1,:,:]
edgesA = stats.threshold(edgesA, threshmax=0, newval=255)
cv2.imshow("All Edges", edgesA)
cv2.moveWindow("All Edges", 900, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Use white on black

image = np.zeros((450,450,3), np.uint8)
cv2.circle(image, (100, 200), 50, white, 5)
cv2.rectangle(image, (200,200), (300,400), white, -1)
cv2.imshow("Image", image)
cv2.moveWindow("Image", 0, 0)

edges = image[1:,1:,:] - image[:-1,:-1,:]
edges = stats.threshold(edges, threshmax=0, newval=255)
cv2.imshow("Partial Edges", edges)
cv2.moveWindow("Partial Edges", 450, 0)

edgesH = image[1:,:,:] - image[:-1,:,:]
edgesV = image[:,1:,:] - image[:,:-1,:]
edgesA = edgesH[:,:-1,:] + edgesV[:-1,:,:]
edgesA = stats.threshold(edgesA, threshmax=0, newval=255)
cv2.imshow("All Edges", edgesA)
cv2.moveWindow("All Edges", 900, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Use black on white

image = 255*np.ones((450,450,3), np.uint8)
cv2.circle(image, (100, 200), 50, black, 5)
cv2.rectangle(image, (200,200), (300,400), black, -1)
cv2.imshow("Image", image)
cv2.moveWindow("Image", 0, 0)

edges = image[1:,1:,:] - image[:-1,:-1,:]
edges = stats.threshold(edges, threshmax=0, newval=255)
cv2.imshow("Partial Edges", edges)
cv2.moveWindow("Partial Edges", 450, 0)

edgesH = image[1:,:,:] - image[:-1,:,:]
edgesV = image[:,1:,:] - image[:,:-1,:]
edgesA = edgesH[:,:-1,:] + edgesV[:-1,:,:]
edgesA = stats.threshold(edgesA, threshmax=0, newval=255)
cv2.imshow("All Edges", edgesA)
cv2.moveWindow("All Edges", 900, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()

#matplotlib commands, not using right now
#plt.imshow(image)
#plt.show()






