from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

model = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    global model

    if model is None:
        model = pickle.load(open("teja.pkl", "rb"))

    study = int(request.form["study"])
    social = int(request.form["social"])
    attendance = int(request.form["attendance"])
    sleep = int(request.form["sleep"])

    prediction = model.predict([[study, social, attendance, sleep]])

    return render_template("index.html", result=round(prediction[0], 2))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

