import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import os

def create_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(3, activation='softmax')  # 3 classes: Oil, Screen, Stain
    ])
    return model

def train_model():
    # ... (rest of the training code remains the same)

    # Save the model
    model.save('../../models/phone_defect_model.keras', save_format='keras')

    # ... (rest of the code remains the same)

if __name__ == "__main__":
    train_model()