# Credit Card Fraud Detection

This project is a web application for detecting potential credit card fraud based on user input. Built using Flask for the backend and a pre-trained Random Forest model, the app takes transaction details and predicts the likelihood of fraud.

## Key Features
- **Seamless User Interaction**: An intuitive front-end interface allows users to easily input transaction details for fraud prediction.
- **Efficient Data Handling**: Transaction data is dynamically extracted and sent as JSON to the Flask backend, ensuring smooth communication between the front and back end.
- **Robust Backend Prediction**: Powered by Flask and a highly accurate pre-trained Random Forest model (`RF_model.pkl`), the backend delivers quick and reliable fraud predictions.
- **Instant Fraud Detection**: Users receive real-time predictions on potential fraud, directly displayed on the webpage for immediate insights.

## Input Fields
- **Category**: Type of transaction.
- **Amount**: Transaction amount.
- **Gender**: M/F.
- **Region**: Geographical region of the user.
- **Date of Birth**: Date of birth of credit card holder.
- **Transaction Time and Date**: Details of when the transaction was done.

## How it Works
1. **Data Collection**: All the essential transaction details are collected through an intuitive form, capturing the key features that will determine the likelihood of fraud.
2. **Smart Data Processing**: The gathered information is intelligently manipulated and formatted before being sent to the Flask backend in JSON format, ensuring seamless data flow.
3. **Model-Ready Transformation**: In the backend, the data is meticulously prepared and transformed to meet the model’s input requirements, optimizing the prediction process.
4. **Real-Time Fraud Prediction**: The Random Forest model swiftly evaluates the input, predicting the fraud risk, and the result is instantly displayed on the screen for the user to act upon.


## Technologies
- Flask (Backend)
- Scikit - learn (Modelling)
- HTML/CSS/JavaScript (Frontend)
- Pandas (Data processing)
- MatplotLIB and seaborn (Data Visualisation)
- numpy (Data preprocessing)

## Setup
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd credit-card-fraud-detection
2. Install the Dependencies
   ```bash
   pip install -r requirements.txt
3. Run the flask app
   ```bash
   flask run


   
