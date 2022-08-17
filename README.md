# An end to end project on image classification.
Image classification of six famous footballers; Cristiano Ronaldo, Karim Benzema, Lionel Messi, Mohammed Salah, Robert Lewandoski and Zlatan Ibrahimović.

### The project features:
##### Data Cleaning
In image classification, especially one for classifying people, the most important part of an image is usually the face.  
Hence, data cleaning in image classification is usually getting the relevant part of an image then discarding the 
irrelevant parts of it. In this case, cropping the face of the person in the image an discarding the rest of it. 
##### Feature Engineering
Extracting features from an image is achievable by treating said image as a 2D signal and understanding the image frequency. In a very basic way, one can define the frequency of an image as the changes in the grayscale value of pixels accross the image. 
##### Model training
CNNs models are generally used for image classification but I decided to use SVM classifier. 
##### Web app development
A web app in which you can drag and drop an image and get a classification result.
##### Model deployment to AWS
Hosted the web app on AWS EC2 instance [here](http://ec2-44-203-185-121.compute-1.amazonaws.com/)
