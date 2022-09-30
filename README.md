# An end to end project on image classification.
Image classification of six famous footballers; Cristiano Ronaldo, Karim Benzema, Lionel Messi, Mohammed Salah, Robert Lewandoski and Zlatan Ibrahimović.  
![ballie4](https://user-images.githubusercontent.com/91638505/193248988-965cd78b-e0ae-41d9-b9b8-361a99e8f9e3.png)
![ballie2](https://user-images.githubusercontent.com/91638505/193249103-c9bd48a8-f7d9-4380-8dea-b109ebdac2c5.png)


### The project features:
##### Data Cleaning
In image classification, especially one for classifying people, the most important part of an image is usually the face.  
Hence, data cleaning in image classification is usually getting the relevant part of an image then discarding the 
irrelevant parts of it. In this case, cropping the face of the person in the image an discarding the rest of it.  The notebook for data cleaning is available [here](https://github.com/ifunanyaScript/FootballStars-image-classification/blob/main/notebooks/data_cleaning.ipynb), I'm you're keen to check it out.

##### Feature Engineering
Extracting features from an image is achievable by treating said image as a 2D signal and understanding the image frequency. In a very basic way, one can define the frequency of an image as the changes in the grayscale value of pixels accross the image. To get more explication on this, check out my feature engineering notebook [here](https://github.com/ifunanyaScript/FootballStars-image-classification/blob/main/notebooks/feature_engineering.ipynb).

##### Model training
Normally, The go to for computer vision is CNNs however, there are other approaches that could suffice and even achieve amazing accuracy.
Apparently, this is a classification problem, hence I used an SVM classifier as the model. The model was trained with over 500 images of the 6 footballers. The model achieved over 91% accuracy on the test dataset. The notebook for model building is available [here](https://github.com/ifunanyaScript/FootballStars-image-classification/blob/main/notebooks/model_development.ipynb).  
ALso the trained model was saved and exported as a pickle file. The file is available [here](https://github.com/ifunanyaScript/FootballStars-image-classification/blob/main/model/model.pickle).

##### Web app development
A web app in which you can drag and drop an image of one of the featured six footballers and get a classification result.  
All the source codes and files used to develop the web app is available [here](https://github.com/ifunanyaScript/FootballStars-image-classification/tree/main/client).

##### Python Flask server
I built a backend server using python Flask. This server recieves requests from the frontend, and returns a response.  
In the server the pre trained model and other essential artifacts are loaded. Whenever a request(image) comes in, the server directs the image to the model.  
The model spits out a classification result which the server in turn returns to the front end.  
The server and it's dependencies are available [here](https://github.com/ifunanyaScript/FootballStars-image-classification/tree/main/server).

##### Model deployment to AWS
Using Python Flask server and nginx web server, I hosted the web app on AWS EC2 instance [here](http://ec2-44-203-185-121.compute-1.amazonaws.com/).  
<br>
<br>
<br>
Apparently, there were series of stages passed to achieve the final result of this project. All the jupyter notebooks and source codes used to work on the project are 
all available in this repository. Feel free to fork this repo.  
Drop a ⭐ on your way out, Thanks!
