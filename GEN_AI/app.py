from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

# Sample data for training
data = {
    'area': [1000, 1500, 1800, 2400, 3000, 3500],
    'bedrooms': [2, 3, 3, 4, 4, 5],
    'age': [10, 5, 3, 20, 15, 7],
    'price': [200000, 300000, 350000, 400000, 450000, 500000]
}

df = pd.DataFrame(data)
X = df[['area', 'bedrooms', 'age']]
y = df['price']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    age = int(request.form['age'])

    input_data = pd.DataFrame([[area, bedrooms, age]], columns=['area', 'bedrooms', 'age'])
    prediction = model.predict(input_data)[0]

    return render_template('index.html', prediction_text=f'Predicted House Price: ₹{prediction:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)
