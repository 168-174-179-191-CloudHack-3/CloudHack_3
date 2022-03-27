from flask import Flask, render_template, request, flash, redirect, url_for,Response
from flask_restful import Api,Resource
import requests
import json
import os
import math

app = Flask(__name__)
api = Api(app)

class LCM(Resource):
   def get(self,arg1,arg2):
       n1 = int(arg1)
       n2 = int(arg2)
       res = (n1*n2)/(math.gcd(n1,n2))
       return Response(
           response = json.dumps({"result":res}),
           status = 200
       )

api.add_resource(LCM,"/lcm/<int:arg1>/<int:arg2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5057,
        host="0.0.0.0"
    )