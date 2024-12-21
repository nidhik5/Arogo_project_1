**Overview**

This project aims to build an AI model to predict whether a shipment will be delayed or on time based on historical data from the logistics domain. The dataset includes information about the shipment's origin, destination, shipment date, vehicle type, distance, weather conditions, traffic conditions, and the actual delay status of the shipment. The model will assist logistics companies in predicting shipment delays and optimizing delivery processes.

**Problem Statement**

The goal is to develop a machine learning model that predicts whether a shipment will be delayed or on time based on several input features. This project involves data cleaning, exploratory data analysis (EDA), model development, evaluation, and deployment of a prediction API.

**Dataset Details**

The dataset includes the following columns:
Shipment ID: Unique identifier for each shipment (not used in prediction).
Origin: The origin city of the shipment (Indian cities).
Destination: The destination city of the shipment (Indian cities).
Shipment Date: The date the shipment was dispatched.
Planned Delivery Date: The planned date for delivery.
Actual Delivery Date: The actual date the shipment was delivered.
Vehicle Type: Type of vehicle used for the shipment (Truck, Lorry, Container, Trailer).
Distance (km): Distance traveled by the shipment in kilometers.
Weather Conditions: The weather during the shipment (Clear, Rain, Fog).
Traffic Conditions: The traffic conditions during the shipment (Light, Moderate, Heavy).
Delayed: The target variable, indicating whether the shipment was delayed (Yes/No).

**Objective**

*Data Cleaning & Preprocessing*: Prepare the data by handling missing values, encoding categorical variables, and scaling numerical features.
*Model Development*: Train machine learning models (Logistic Regression, Random Forest, and others) to predict shipment delays.
*Model Evaluation*: Evaluate the models using metrics such as accuracy, precision, recall, F1 score, and ROC-AUC.
*Deployment*: Deploy the model via an API (Flask/FastAPI) to make predictions based on new shipment data.
