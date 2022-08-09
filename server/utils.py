import numpy as np
import cv2
import pickle
import json
import base64
from wavelet import wavelet2D

__label_name_number = {}
__label_number_name = {}
__model = None

def get_b64_image():
    with open(r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\server\base64.txt") as f:
        return f.read()

def base64_to_image(base64_string):
    encoded_data = base64_string.split(",")[1]
    nparray = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    image = cv2.imdecode(nparray, cv2.IMREAD_COLOR)
    return image

def get_clean_image(base64_string, file_path):
    detect_face = cv2.CascadeClassifier(r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\opencv\haarcascade_frontalface_default.xml")
    detect_eye = cv2.CascadeClassifier(r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\opencv\haarcascade_eye.xml")

    if file_path:
        image = cv2.imread(file_path)
    else:
        image = base64_to_image(base64_string)
    
    if image is not None:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face = detect_face.detectMultiScale(gray_image, 1.3, 5)

        cropped_faces = []
        for (x, y, w, h) in face:
            region_gray = gray_image[y:y+h, x:x+w]
            region_colour = image[y:y+h, x:x+w]
            eyes = detect_eye.detectMultiScale(region_gray)
            # Check if there are two eyes
            if len(eyes) >= 2:
                # Append face if it has two eyes.
                cropped_faces.append(region_colour)
    return cropped_faces

def load_aritifacts():
    print(f"Loading Artifacts...")
    global __label_name_number
    global __label_number_name

    with open(r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\model\artifacts\label_dict.json", "r") as f:
        __label_name_number = json.load(f)
        __label_number_name = {i:k for k,i in __label_name_number.items()}
        
    global __model
    with open(r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\model\artifacts\model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Artifacts succesfully loaded!")

def number_name(label_number):
    return __label_number_name[label_number]

def classify_image(base64_image, file_path=None):
    images = get_clean_image(base64_image, file_path)

    prediction = []

    for image in images:
        # Simply resize the original image, get the wavelet transform image and vertically stack both of them.
        resized_image  = cv2.resize(image, (32, 32))
        wavelet_image = wavelet2D(image, Wname="haar", level=5)
        resized_wavelet_image = cv2.resize(wavelet_image, (32, 32))
        stacked_image = np.vstack((resized_image.reshape(32*32*3, 1), resized_wavelet_image.reshape(32*32, 1)))
        
        len_imagearr = (32*32*3) + (32*32)
        ultimate = stacked_image.reshape(1, len_imagearr).astype(float)

        prediction.append({
            "label": number_name(__model.predict(ultimate)[0]),
            "label_probability": np.around(__model.predict_proba(ultimate)*100, 2).tolist()[0],
            "label_dict": __label_name_number
        })

    return prediction



if __name__ == "__main__":
    load_aritifacts()
    print(classify_image(get_b64_image(), None))
    # print(classify_image(None, file_path=r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\data\misc_data\cr2.jpg"))
    # print(classify_image(None, file_path=r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\data\misc_data\kb1.jpg"))
    # print(classify_image(None, file_path=r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\data\misc_data\kb2.jpg"))
    print(classify_image(None, file_path=r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\data\misc_data\lm1.jpg"))
    print(classify_image(None, file_path=r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\data\misc_data\mo1.jpg"))
    print(classify_image(None, file_path=r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\data\misc_data\mo2.jpg"))
    print(classify_image(None, file_path=r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\data\misc_data\rl1.jpg"))
    print(classify_image(None, file_path=r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\data\misc_data\rl2.jpg"))
    print(classify_image(None, file_path=r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\data\misc_data\rl3.jpg"))
    print(classify_image(None, file_path=r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\data\misc_data\zi1.jpg"))
    print(classify_image(None, file_path=r"C:\Users\ifunanyaScript\Everything\FootballStars_image_classification\data\misc_data\zi2.jpg"))