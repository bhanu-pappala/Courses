from tensorflow import keras
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('acc') > 0.7:
            print("\nReached 70% accuracy so cancelling training!")
            self.model.stop_training = True


callbacks = myCallback()

mnsit = keras.datasets.fashion_mnist

(training_images, training_labels), (test_images, test_labels) = mnsit.load_data()

plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])

training_images = training_images / 255.0
test_images = test_images / 255.0

model = tf.keras.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)),
                             tf.keras.layers.Dense(128, activation=tf.nn.relu),
                             tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer=tf.keras.optimizers.Adam(), loss='sparse_categorical_crossentropy',metrics=['accuracy'])

mod = model.fit(training_images, training_labels, epochs=10, callbacks=[callbacks])

eval = model.evaluate(test_images, test_labels)

print(mod)

