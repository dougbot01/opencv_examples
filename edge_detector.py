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


#plt.imshow(image)
#plt.show()






