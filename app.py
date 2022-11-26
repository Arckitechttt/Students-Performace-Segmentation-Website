import os
import numpy as np
import flask
import pickle
from flask import Flask, redirect, url_for, request, render_template


# creating instance of the class
app = Flask(__name__, template_folder='templates')

# to tell flask what url should trigger the function index()


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 2)
    loaded_model = pickle.load(
        open("./model/model.pkl", "rb"))  # load the model
    # predict the values using loded model
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        annual_income = request.form['annual_income']
        spending_score = request.form['spending_score']

        to_predict_list = list(map(float, [annual_income, spending_score]))
        result = ValuePredictor(to_predict_list)

        if float(result) == 0:
            prediction = 'You are customers with medium annual income and medium annual spend'
        elif float(result) == 1:
            prediction = 'You are customers with medium to high annual income and low annual spend'
        elif float(result) == 2:
            prediction = 'You are customers with low annual income and low annual spend'
        elif float(result) == 3:
            prediction = 'You are customers with low annual income and high annual spend'
        elif float(result) == 4:
            prediction = 'You are customers with medium to high annual income and high annual spend'

        return render_template("result.html", prediction=prediction, name=name)


if __name__ == "__main__":
    app.run(debug=False)