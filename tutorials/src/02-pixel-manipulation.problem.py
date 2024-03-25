# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place,
# count the used colors in the image

import cv2
import numpy as np

# TODO Loading images in grey and color
img_gray = cv2.imread("tutorials\data\images\logo.png", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("tutorials\data\images\logo.png", cv2.IMREAD_COLOR)
# TODO Do some print out about the loaded data using type, dtype and shape
#Type
print(type(img_gray))
print(type(img_color))
#dtype
print(img_gray.dtype)
print(img_color.dtype)
#shape
print(img_gray.shape)
print(img_color.shape)
# TODO Continue with the grayscale image
img = img_gray
# TODO Extract the size or resolution of the image
h, w =img.shape
print("Width =", w)
print("Height =" ,h)
# TODO Resize image
img = cv2.resize(img, (8,4))
# Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for general access on ndarrays
# TODO Print first row
print(img[0,:])
# TODO Print first column
print(img[:,0])
# TODO Continue with the color image
img = img_color
print(img.shape)
# TODO Set an area of the image to black [rows=Zeilen -> colums-Spalten]
img[50:100,:] = (0,0,0)
# TODO Show the image and wait until key pressed
cv2.imshow("My Image", img)
cv2.waitKey(0)

# TODO Find all used colors in the image
print()

# TODO Copy one part of an image into another one

# TODO Save image to a file

# TODO Show the image again

# TODO Show the original image (copy demo)
