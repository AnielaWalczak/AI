import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import random


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer ='adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(x_train, y_train, epochs = 3)
model.save('handwritten.model')

model = tf.keras.models.load_model('handwritten.model')
numery_paczek=[]

def liczby():
    digits=[]
    for i in range(0, 3):
        image_number = random.randint(1, 19)
        img = cv2.imread(f"digits/digit{image_number}.png")[:, :, 0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"This digit is probably a {np.argmax(prediction)}")
        digits.append(np.argmax(prediction))
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    liczba = int(str(digits[0]) + str(digits[1]) + str(digits[2]))
    if liczba in numery_paczek or liczba < 100:
        liczby()
    else:
        numery_paczek.append(liczba)
    return numery_paczek[-1]

def recognition():
    try:
        liczba= liczby()
    except:
        print("Error!")
    ostatnia = liczba % 10
    loss, accuracy = model.evaluate(x_test, y_test)
    print(loss)
    print(accuracy)
    print(numery_paczek)
    return ostatnia
