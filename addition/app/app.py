from flask import Flask, render_template, request, flash, redirect, url_for
import json
import requests
import os
from flask_restful import Api, Resource, reqparse

class Addition(Resource):

        
    def get(self,arg1,arg2):
        return {'result': arg1+arg2}

app = Flask(__name__)
api = Api(app)
api.add_resource(Addition,'/<int:arg1>/<int:arg2>')

if __name__ == '__main__':
    app.run(debug=True,port=5050,host="0.0.0.0")
