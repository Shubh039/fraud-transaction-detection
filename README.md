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

## Dataset
The dataset used in this project consists of 555,719 records and 23 features, capturing various aspects of credit card transactions. Key columns include transaction date and time, amount, merchant details, and demographic information such as gender and job. The dataset also includes geolocation data and a target variable, `is_fraud`, indicating whether the transaction is fraudulent. This comprehensive dataset allows for detailed analysis and accurate fraud detection modeling.


## Approach and Model Building

### Feature Engineering
To enhance the predictive power of the model, several key features were engineered from the dataset:

1. **Geographical Distance**: Calculated the distance between the merchant and the transaction location using the geographical coordinates, adding a crucial layer of spatial context.
2. **Age Groups**: Derived age groups from the date of birth and transaction date, categorizing users into ranges such as "14-18", "18-35", "35-60", and "60+" to capture demographic trends.
3. **Day Period**: Identified the time of day when the transaction occurred, segmenting it into periods like morning, afternoon, and evening to capture temporal patterns in transaction behavior.
4. **Job Sector Classification**: Simplified job titles into broader sectors to reduce complexity and enhance model performance by focusing on general employment categories.
5. **Regional Grouping**: Grouped transactions into regions based on the state to streamline categories and improve understanding, facilitating better analysis.

Additionally, irrelevant columns were removed to focus the dataset on the most impactful features, ensuring a more efficient and accurate model training process.

## Data Visualization

To better understand the dataset and the impact of engineered features, several visualizations were created:

### Key Insights
1. **Gender Analysis**: Although there's no significant difference in the proportion of fraud victims based on gender, women engage in a higher volume of transactions (709,863) compared to men (586,812). The fraud rate is slightly higher for men at 0.64%, compared to 0.53% for women.
   
2. **Age Group Trends**: Teenagers are the least likely to experience credit card fraud, possibly due to limited credit card usage. Middle-aged individuals show higher vulnerability, as indicated by the bar chart, which may be linked to their frequent use of credit cards. Fraud is most prevalent among those aged 60 and above, with a rate of 0.75%, potentially due to lower digital literacy.

### Categorical Data Observations
- **Gender**: The dataset shows a higher number of female transactions.
- **Transaction Timing**: Weekend transactions are roughly half as frequent as weekday transactions.
- **Time of Day**: A significant volume of transactions occur at night.
- **Age Vulnerability**: Middle-aged individuals are more susceptible to fraud.

### Numerical Data Insights
- **Correlation**: Both 'amt' and 'distance' features had similar correlations with the target column. To avoid redundancy, 'distance' was dropped from the dataset.

### Visualized Features
- **Categorical Features**: category, gender, is_fraud, Region, job_sector, age_group, and day_period.
- **Numerical Features**: amt, distance.

These visualizations provided valuable insights into the patterns and relationships within the data, guiding the feature engineering and model-building process.

## Modeling with Random Forest

The final stage of the project involved building and training a Random Forest model to detect fraudulent transactions. Here’s a detailed look at the process:

### Final Input Features
The model was trained using the following input features:
- **Category**: Type of transaction.
- **Amount (amt)**: Transaction amount.
- **Gender**: Gender of the cardholder.
- **Age Group (age_group)**: Defined age ranges of the cardholder.
- **Day Period (day_period)**: Time of day when the transaction occurred.
- **Region**: Geographical region of the transaction.

The target label for prediction is **`is_fraud`**, indicating whether the transaction is fraudulent.

### One-Hot Encoding
To handle categorical variables, One-Hot Encoding was applied using `pd.get_dummies()` to convert categorical features into a format suitable for machine learning algorithms.

### Model Training
A Random Forest Classifier was used for its robustness and ability to handle imbalanced datasets. The model was trained with class weights balanced to account for the discrepancy between fraudulent and non-fraudulent transactions. The model’s balanced class weight parameter ensures that both fraudulent and non-fraudulent transactions are given appropriate consideration during training.

## Model Evaluation

The performance of the Random Forest model was rigorously evaluated to ensure its accuracy and effectiveness in detecting fraudulent transactions. Here’s an overview of the evaluation results:

### Accuracy
The model achieved an impressive accuracy of **99.995%** on the test data. This exceptionally high accuracy indicates that the model correctly identifies nearly all transactions, both fraudulent and non-fraudulent.

### Confusion Matrix
The confusion matrix is presented in the table below:

|                | Predicted Non-Fraud | Predicted Fraud |
|----------------|---------------------|-----------------|
| **Actual Non-Fraud** | 553,548             | 26              |
| **Actual Fraud**     | 1                   | 2,144           |

- **True Negatives (553,548)**: Correctly identified non-fraudulent transactions.
- **False Positives (26)**: Non-fraudulent transactions incorrectly classified as fraudulent.
- **False Negatives (1)**: Fraudulent transactions incorrectly classified as non-fraudulent.
- **True Positives (2,144)**: Correctly identified fraudulent transactions.

## Conclusion

In this project, we developed a robust credit card fraud detection system using a Random Forest model. Through meticulous feature engineering and data preprocessing, we engineered key features that enhanced the model’s predictive performance. 

The model was evaluated with an impressive accuracy of 99.995%, demonstrating its reliability in identifying both fraudulent and non-fraudulent transactions. The confusion matrix highlights the model's effectiveness, with minimal false positives and false negatives, ensuring accurate and timely fraud detection.

This project showcases the power of combining advanced machine learning techniques with thorough data analysis to tackle real-world challenges. The system is designed to provide reliable fraud detection, helping to safeguard financial transactions and enhance security measures.

Thank you for exploring this project. For further details or to contribute, please feel free to reach out via email at [SHUBHANK SHARMA](mailto:shubhanks039@gmail.com) or review the code in the repository.




   
