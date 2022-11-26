# ImportLibraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, redirect, url_for, request, render_template


# Instance of the class
app = Flask(__name__, template_folder='templates')

# Telling Flask that the indexx.html should trigger the function index()
@app.route('/')
@app.route('/indexx')
def indexx():
    AuthorName = "Arckitecht"
    return render_template("indexx.html", user=AuthorName)


# Creating a function which is Predictor(predict_list) that contains 1 parameter which is predict_list
def Predictor(predict_list):
    predictt = np.array(predict_list).reshape(1, 2)
    loaded_model = pickle.load(
        open("./model/model.pkl", "rb"))  # Load the model
    # Predict the values using Loaded Model
    result = loaded_model.predict(predictt)
    return result[0]

# Creating a function to show the result from our Clustering Model
@app.route('/resultt', methods=['POST'])
def resultt():
    if request.method == 'POST':
        name = request.form['name']
        mathscore = request.form['mathscore']
        readingscore = request.form['readingscore']

        predict_list = list(map(float, [mathscore, readingscore]))
        result = Predictor(predict_list)

        if float(result) == 0:
            prediction = 'You Are an Excellent Student!'
            grade = 'Your Grade is A'
        elif float(result) == 1:
            prediction = 'Your Are a Good Student!'
            grade = 'Your Grade is B'
        elif float(result) == 2:
            prediction = 'Your Are a Fucking Stupid Idiot Autistic Student!'
            grade = 'Your Grade is C'

        return render_template("resultt.html", prediction=prediction, name=name, grade=grade)


if __name__ == "__main__":
    app.run(debug=True)