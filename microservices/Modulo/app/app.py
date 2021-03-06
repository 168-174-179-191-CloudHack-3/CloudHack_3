from flask import Flask, render_template, request, flash, redirect, url_for,Response
from flask_restful import Api,Resource
import requests
import json
import os
import math

app = Flask(__name__)
api = Api(app)

class Modulo(Resource):
   def get(self,arg1,arg2):
       res = int(arg1)%int(arg2)
       return Response(
           response = json.dumps({"result":res}),
           status = 200
       )

api.add_resource(Modulo,"/modulo/<string:arg1>/<string:arg2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5056,
        host="0.0.0.0"
    )