# CO-BEAT

A web application to fight covid-19 using Machine learning.

Through CO-BEAT you can find information about covid-19 - symptoms and prevention measures, 
get an overview of covid cases in India using the dashboard, view contact tracing alerts, predict covid-19 from chest x-ray and cough sound.

## Description

* **index.html** - home page which contains links to all the other pages.
* **aboutcovid.html** - contains symptoms and preventive measures for Covid.
* **contact_tracing_alerts.html** - displays a table with venues and datetime of places visited by people who tested positive.Data is fetched from the sqlite3 database.
* **cough_sound_detection.html** - takes audio input and detects the presence of coronavirus.
* **covid_dashboard.html** - shows the covid-19 INDIA data which contains daywise confirmed, recovered and deaths and total cases in each state of country
* **detection.html** - takes chest xray as input and detects coronavirus.

* **Cough-sound-based-prediction** folder has algorithms used to detect covid from cough sound.
Method1 is using PyAudioanalysis and Method2 is with a neural network model.The former had higher accuracy and was used for prediction in the website.
The datasets used were COUGHVID and COSWARA. As the number of covid cough sound samples were less, data augmentation was done using Audiomentations library.  
Training : 2017 samples, Testing : 252 samples

    | Method | Accuracy |
    | --- | --- |
    | PyAudioAnalysis with SVM | 74% |
    | Neural network | 67% |  
  
* **Covid-Prediction-Chest-Xray** folder has the code from generating models using 3 ways

    1. Using pre-trained Densenet121 for feature extraction followed by svm for classification
    2. Using pre-trained Densenet169 for feature extraction followed by svm for classification
    3. Fine tuning pre-trained Densenet121 for classification.This model was used in website.

    The dataset used was Covid-19 Radiography dataset.  
    Training : 3280 samples, Testing : 615 samples, Validation : 205 samples

    | Method | Accuracy (Classification as Covid or non-covid) |
    | --- | --- |
    | Densenet121 with SVM | 96.16% |
    | Densenet169 with SVM | 96.45% |
    | Densenet121 fine tuned | 95.93% |  

## Software Requirements

Keras  
Tensorflow version 2.4.1  
Sklearn version 0.23.1  
PyAudioAnalysis  
Python  
Numpy  
Django  

## Process Flow



## Data Flow Diagram

## References

https://arxiv.org/abs/2011.13320  
https://www.pyimagesearch.com/2019/02/04/keras-multiple-inputs-and-mixed-data/  
https://pypi.org/project/audiomentations/  



