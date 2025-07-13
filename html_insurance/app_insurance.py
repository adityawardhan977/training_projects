from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = int(request.form['smoker'])
        region = int(request.form['region'])


if __name__ == "__main__":
    app.run(debug=True)