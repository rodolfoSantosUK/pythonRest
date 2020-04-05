from flask import Flask, request, jsonify
from flask_restful import Api, Resource

"""
Para importar flask_restful:
No diretório do projeto colocar :
pip3 install flask-restful
python3
import flask_restful as fr

"""

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName ):
    if(functionName == "add"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200

class Add(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, "add")
        if(status_code != 200):
            retJson = {
                "Message" : "An error happened",
                "Status Code" : status_code
            }
            return jsonify(retJson)


        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x + y

        retMap = {
            "Message" : ret,
            "Status Code" : status_code
        }
        return jsonify

api.add_resource(Add,"/add")

