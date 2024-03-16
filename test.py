from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
model = load_model("apple_banana_classifier.h5")
IMG_WIDTH, IMG_HEIGHT = 100, 100
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(IMG_WIDTH, IMG_HEIGHT))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

image_path = "mypic.jpg"  # Replace with the path to your new image
preprocessed_image = preprocess_image(image_path)

predictions = model.predict(preprocessed_image)
class_index = np.argmax(predictions)

if class_index == 0:
    print("This is an apple.")
else:
    print("This is a banana.")