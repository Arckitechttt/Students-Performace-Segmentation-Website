import crypt.methods
import imp
from pyexpat import features

from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/',methods=["GET","POST"])

def home():
    AuthorName = "Arckitecht"
    return render_template("home.html", user=AuthorName)

@app.route('/cryo-model',methods=["POST"])
def cryomodel():
    float_features = [float(x) for x in request.form.values()]
    feature = [np.array(float_features)]
    prediction = model.predict(feature)
    return render_template("cryo-model.html", prediction_text="{}".format(prediction))

if __name__ == '__main__':
    app.run(debug=True)