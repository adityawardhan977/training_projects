from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/project', methods = ["POST", "GET"])
def predict():
    if request.method=='POST':
        brand_name=request.form['brand_name']
        owner=request.form['owner']
        age=request.form['age']
        power=request.form['power']
        kms_driven=request.form['kms_driven']
        print("My Data >>>>>>>>>>>>", brand_name, age, power, kms_driven, owner)
    return render_template('project.html')

if __name__ == "__main__":
    app.run(debug=True)
