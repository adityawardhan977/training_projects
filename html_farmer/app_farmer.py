from flask import Flask, request, render_template
from joblib import load
import numpy as np

app = Flask(__name__)

# Load your trained model
model = load('model_farmer.joblib')

# Mapping numeric label to crop name
label_dict = {
    0: "Rice",
    1: "Wheat",
    2: "Maize",
    3: "Sugarcane",
    4: "Cotton",
    5: "Barley",
    6: "Millets",
    7: "Peas",
    8: "Groundnut",
    9: "Soybean",
    10: "Lentil"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect inputs from form
        features = [
            float(request.form['N']),
            float(request.form['P']),
            float(request.form['K']),
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['ph']),
            float(request.form['rainfall'])
        ]
        features_array = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features_array)[0]
        crop_name = label_dict.get(round(prediction), "Unknown")

        return render_template('index.html', prediction_text=f"✅ Recommended Crop: {crop_name}")
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"❌ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
