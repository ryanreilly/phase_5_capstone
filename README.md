# Natrual Disaster Classification

**Author:** Ryan Reilly
![title](images/disaster_1.jpeg)

## Overview

This project analyzes almost 17,000 images related to natural disasters.  Human labelers labeled these images and then the images were into a downloadable format from the Crisis NLP website. Crisis NLP makes resources available to help researchers and technologists  advance research on humanitarian and crisis computing. I will be using the disaster type dataset. There were two original datasets that were collected for disaster types images:

1. Damage Multimodel Dataset (DMD). Method used to collect: crawled images from Google and Instagram based on 100 different hashtags related to crisis lexicon.

2. AIDR Disaster Type Dataset (AIDR-DT) Method used to collect: tweets were collected from 17 disaster events, and then using the annotations of the tweet, they crawled images from bing, google and flickr.  

The goal of this analysis is to build a model that will accurately predict the disaster type of the image scraped off the internet. This will be done through exploratory data analysis and iterative predictive modeling using classification models. 

## Business Problem

During a disaster event, images shared on social media helps government organizations gain situational awareness and assess incurred damages, among other response tasks. By classifying images of natural disasters, this model would aim to help organizations like FEMA augment data they are already receiving about a disaster. This would allow FEMA to disseminate more information down to crisis managers so the correct resources are deployed to the disater quicker, thus saving more lives. 

## Data Understanding

The data comes in two types of files. There is a folder of images and 3 tsv files that shows the path of each image for the train, validation, and test splits. The data was downloaded from this website: https://crisisnlp.qcri.org/crisis-image-datasets-asonam20. Below are the columns and their description of each tsv file. 

| Feature | Description|
|:-------| :-------|
|event_name| Name of original dataset used. Either AIDR or DMD|
|image_id| Unique ID for each image|
|image_path| Folder structure path of where the image is stored|
|class_label|Disaster type|

### Methods

* Preliminary exploratory data analysis to identify the distribution of images across the disaster type classes, the outcome we are trying to predict
* Preprocessing images by rescaling and and passing in data augmentation parameters to be used for modeling
* Building and evaluating model performance for a baseline CNN model
* Moving to the cloud to take advantage of accelerated hardware used for transfer learning CNN models built on pre-trained CNN architectures. 
* Selecting final model and creating an app that will predict the disaster type based on an image scraped from Twitter

### Exploratory Data Analysis and Feature Engineering 
![title](images/classes_count.png)

The chart above shows the count of images for each of the classes. There looks to be a good amount of training images for all 7 classes. However, there does look to be a class imbalance, especially with the Not Disaster images having considerably more images. I will deal with this by experimenting with adding weights to the CNN models I train.

![title](images/distribution_splits.png)

I created the above charts just to visually inspect the images counts across each folder. The train, validation and test folders look to have the same distribution of images over each class. The train/validation/test splits for these images are 70/10/20 respectively.



