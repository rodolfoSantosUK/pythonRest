from flask import Flask, request, jsonify 

app = Flask(__name__)


@app.route('/add_two_numbers', methods=["GET","POST"])
def add_two_nums():
    dataDict = request.get_json()

    if "y" not in dataDict:
        return "ERROR", 305

    x = dataDict["x"]
    y = dataDict["y"]

    z = x + y

    retJSON = {
        "z":z
    }

    return jsonify(retJSON), 200

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi_there_everyone ():
    return 'I just hit /hithere'

@app.route('/bye')
def bye():
     c=2*534
     s=str(c)
     return bye ;

if __name__=="main":
    app.run(host="0.0.0.1")

  # export FLASK_APP = app.py
  # flask run
