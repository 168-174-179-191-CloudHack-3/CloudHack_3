from flask import Flask, render_template, request, flash, redirect, url_for,Response
from flask_restful import Api,Resource
import requests
import json
import os

app = Flask(__name__)
api = Api(app)

class Greater(Resource):
    def get(self,arg1,arg2):
        if(int(arg1)>int(arg2)):
            res = True
        else:
            res = False
        return Response(
           response = json.dumps({"result":res}),
           status = 200
       )

api.add_resource(Greater,"/gt/<string:arg1>/<string:arg2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5061,
        host="0.0.0.0"
    )