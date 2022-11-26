from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])

def home():
    AuthorName = "Arckitecht"
    return render_template("home.html", user=AuthorName)

@app.route('/cryo-model',methods=["GET","POST"])
def cryoModel():
    return render_template("cryo-model.html")

if __name__ == '__main__':
    app.run(debug=True)