# Credit Card Fraud Detection

This project is a web application for detecting potential credit card fraud based on user input. Built using Flask for the backend and a pre-trained Random Forest model, the app takes transaction details and predicts the likelihood of fraud.

## Features
- User input form with transaction details.
- JavaScript for calculating age based on `date_of_birth` and `transaction_date_time`.
- Flask backend for model prediction using `RF_model.pkl`.
- Real-time fraud prediction displayed on the webpage.
- Responsive and visually appealing layout.

## Input Fields
- **Category**: Type of transaction.
- **Amount**: Transaction amount.
- **Gender**: M/F.
- **Region**: Geographical region of the user.
- **Age Group**: Predefined age ranges.

## How it Works
1. The user submits transaction details.
2. Age is calculated via JavaScript from `date_of_birth` and `transaction_date_time`.
3. The input is converted to JSON and sent to Flask.
4. Flask processes the input, encodes it, and feeds it to the Random Forest model.
5. The fraud prediction result is displayed on the webpage.

## Technologies
- Flask (Backend)
- Random Forest (Model)
- HTML/CSS/JavaScript (Frontend)
- Pandas (Data processing)

## Setup
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd credit-card-fraud-detection
