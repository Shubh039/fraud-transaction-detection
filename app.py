from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

model = joblib.load('RF_model.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])

    # Perform One-Hot Encoding
    df_encoded = pd.get_dummies(df, columns=["category", "gender", "Region", "age_group", "day_period"], drop_first=False)


    original_columns = [
        'amt', 'category_food_dining', 'category_gas_transport',
        'category_grocery_net', 'category_grocery_pos',
        'category_health_fitness', 'category_home', 'category_kids_pets',
        'category_misc_net', 'category_misc_pos', 'category_personal_care',
        'category_shopping_net', 'category_shopping_pos', 'category_travel',
        'gender_M', 'Region_Midwest', 'Region_Northeast',
        'Region_Rocky Mountains', 'Region_South', 'age_group_18-35',
        'age_group_35-60', 'age_group_60+', 'day_period_Evening',
        'day_period_Morning', 'day_period_Night'
    ]

    df_encoded = df_encoded.reindex(columns=original_columns, fill_value=0)

    # Prediction
    prediction = model.predict(df_encoded)
    print("Prediction:", prediction)

    result = "Fraud" if prediction[0] == 1 else "Not Fraud"
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
