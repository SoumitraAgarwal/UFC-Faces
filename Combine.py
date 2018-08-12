import numpy as np
import cv2
import os

base = 'Categorical/'
folders = os.listdir(base)

for folder in folders:
	print(folder)
	fold = base + folder
	images = os.listdir(fold)
	output 	= cv2.imread(fold + '/' + images[0])
	image1 	= cv2.imread(fold + '/' + images[1])
	cv2.addWeighted(image1, 1.0/len(images) , output, 1.0/len(images), 0, output)
	for i in range(2, len(images)):

		image1 = cv2.imread(base + images[i])
		cv2.addWeighted(image1, 1.0/len(images), output, 1, 0, output)
	cv2.imwrite(base + folder + '.png', output)