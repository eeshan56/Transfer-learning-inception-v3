
from keras.preprocessing import image
from keras.models import load_model

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

label_map = {'butterfly' : 0, 'cat' : 1, 'chicken' : 2, 'cow' : 3, 'dog' : 4, 'elephant' : 5, 'horse' : 6, 'sheep' : 7, 'squirrel' : 8, 'spider' : 9}

def display_img(image_path):
	img = mpimg.imread(image_path)
	imgplot = plt.imshow(img)
	plt.show()

def predict(model, image_path, label_map):
	display_img(image_path)

	img = image.load_img(image_path, target_size = (299, 299))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis = 0)
	x /= 255.

	y_prob = model.predict(x)
	y_classes = y_prob.argmax(axis = -1)

	for i in label_map:
		if label_map[i] == y_classes[0]:
			return i

	return "-1"

image_path = input("Enter img path: ")

model = load_model('model.h5')

print("This is a " + str(predict(model, image_path, label_map)))