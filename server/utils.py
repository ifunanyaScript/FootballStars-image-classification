import numpy as np
import cv2
import pickle
import json
import base64
from wavelet import wavelet2D

def get_clean_image(path, base64_image):
    detect_face = cv2.CascadeClassifier(r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\opencv\haarcascade_frontalface_default.xml")
    detect_eye = cv2.CascadeClassifier(r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\opencv\haarcascade_eye.xml")

    if path:
        image = cv2.imread(path)
    else:
        image = get_image_from_base64_string(base64_image)
    
    if image is not None:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face = detect_face.detectMultiScale(gray_image, 1.3, 5)

        cropped_face = []
        for (x, y, w, h) in face:
            region_gray = gray_image[y:y+h, x:x+w]
            region_colour = image[y:y+h, x:x+w]
            eyes = detect_eye.detectMultiScale(region_gray)
            # Check if there are two eyes
            if len(eyes) >= 2:
                # return the cropped image of the face.
                return region_colour

def classify_image(base64_image, file_path=None):
    pass

def get_image_from_base64_string(base64_string):
    encoded_data = base64_string.split(",")[1]
    nparray = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    image = cv2.imdecode(nparray, cv2.IMREAD_COLOR)
    return image

def get_b64_image():
    with open(".\base64.txt") as f:
        return f.read()

if __name__ == "__main__":
    print(classify_image(get_b64_image(), file_path=None))