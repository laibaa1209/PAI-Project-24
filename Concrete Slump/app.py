from flask import Flask, render_template, request
import pickle
import numpy as np

# Load your trained model (exported as pickle from your Jupyter Notebook)
model = pickle.load(open("concrete_slump_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    water = float(request.form['water'])
    cement = float(request.form['cement'])
    slag = float(request.form['slag'])
    Fly_ash = float(request.form['Fly ash'])
    SP = float(request.form['SP'])
    aggregate = float(request.form['aggregate'])
    Fine_Aggr = float(request.form['Fine Aggregate'])
    flow = float(request.form['flow'])
    compressive_strength = float(request.form['compressive strength'])

    # Create an array for prediction
    features = np.array([[water, cement, slag, Fly_ash, SP, aggregate, Fine_Aggr, flow, compressive_strength]])

    # Predict using the loaded model
    predicted_slump = model.predict(features)[0]

    return render_template('result.html', prediction=round(predicted_slump, 2))

if __name__ == '__main__':
    app.run(debug=True)
