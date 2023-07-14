from keras.applications import resnet50
from keras.models import Sequential
from keras.layers import Dense, GlobalAveragePooling2D
from sklearn.model_selection import train_test_split
import os
import cv2
import numpy as np
from keras.utils import to_categorical

resnet = resnet50.ResNet50(weights='imagenet', include_top=False)
data_path = './cats'
folder_paths = os.listdir(data_path)
labels = [0, 1, 2, 3, 4]

images = []
image_labels = []

for i, folder_path in enumerate(folder_paths):
    files = os.listdir(data_path + '/' + folder_path)
    for file in files:
        image_path = data_path + '/' + folder_path + '/' + file
        image = cv2.imread(image_path)
        image = cv2.resize(image, (224, 224))
        images.append(image)
        image_labels.append(labels[i])

images = np.array(images)
image_labels = np.array(image_labels)
image_labels = to_categorical(image_labels)

train_images,test_images,train_image_labels,test_image_labels = train_test_split(images , image_labels, test_size=0.3, random_state=42)
model = Sequential()
model.add(resnet)
model.add(GlobalAveragePooling2D())
model.add(Dense(256, activation='relu'))
model.add(Dense(5, activation='softmax'))
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
epochs = 50
batch_size = 5
model.fit(train_images, train_image_labels, epochs=epochs, batch_size=batch_size)
loss, accuracy = model.evaluate(test_images, test_image_labels)
model.save('model.h5')


