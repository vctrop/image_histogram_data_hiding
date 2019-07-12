import numpy as np
import cv2
import binascii as basci

class Vector:
	def __init__(self):
		self.imgVec
		self.imgWidth

def imgToVec(img):

	matrix = cv2.imread(img, 0)
	imgVec = matrix.ravel()
	width, height = matrix.shape
	Vector.imgVec = matrix.ravel()
	Vector.imgWidth = width
	return Vector();

def vecToMatrix(vec, width):

	length = len(vec)
	height = int(length/width)
	print(width , height)
	img = vec.reshape(width, height)
	return img;

vector = imgToVec('C:/Users/Michel/Desktop/xablau2.png')

print(vector.imgVec)
print(vector.imgWidth)

img = vecToMatrix(vector.imgVec, vector.imgWidth)

img = cv2.resize(img, (1366, 768))
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


data = "hello"
vect = ''.join(format(ord(x), 'b') for x in data)

print(vect)

data = vect.encode('ascii')

print(data)