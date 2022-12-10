# Import Libraries
import numpy as np
import pandas as pd
import pickle
from flask import Flask, render_template, url_for, redirect
from flask import request as re
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Instance of the class
app = Flask(__name__)

# Telling Flask that the indexx.html should trigger the function index()
@app.route("/")
def index():
    return render_template("indexx.html")

# Machine Learning Processing
def Predictor(predicto):
    sc_reload = pickle.load(open("./model/sc.pkl", "rb"))
    dataSP = sc_reload.transform(predicto)
    
    pca_reload = pickle.load(open("./model/pca.pkl", "rb"))
    principalData = pca_reload.transform(dataSP)
    
    KMeans = pickle.load(open("./model/model.pkl", "rb"))
    result = KMeans.predict(principalData)
    
    return result[0]

# Get the Input, Call and fit the Input to the Predictor() function, and Describe each Clusters
@app.route('/resultt', methods=['POST', 'GET'])
def resultt():
    if re.method == 'POST':
        name = re.form['name']
        parent = re.form['parent']
        lunch = re.form['lunch']
        test = re.form['test']
        math = re.form['math']
        reading = re.form['reading']

        predicto = pd.DataFrame(data=[[parent, lunch, test, math, reading]])
        result = Predictor(predicto)

        if float(result) == 0:
            prediction = "A"
        elif float(result) == 1:
            prediction = "B"
        elif float(result) == 2:
            prediction = "C"
        elif float(result) == 3:
            prediction = "D"
        elif float(result) == 4:
            prediction = "E"
        elif float(result) == 5:
            prediction = "F"

        return render_template("resultt.html", prediction=prediction, name=name)

if __name__ == "__main__":
    app.run(debug=True)
