# Importing necessary libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define constants
IMG_WIDTH, IMG_HEIGHT = 100, 100
input_shape = (IMG_WIDTH, IMG_HEIGHT, 3)
num_classes = 2

# Define the neural network architecture
model = models.Sequential([
    layers.Conv2D(16, (3, 3), activation='relu', input_shape=input_shape),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Data preprocessing
train_datagen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_datagen.flow_from_directory(
        'train_data_directory',  # directory containing training images
        target_size=(IMG_WIDTH, IMG_HEIGHT),
        batch_size=32,
        class_mode='binary')  # assuming you have two classes: apple and banana

# Train the model
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // 32,
    epochs=10)

# Save the model
model.save("apple_banana_classifier.h5")
