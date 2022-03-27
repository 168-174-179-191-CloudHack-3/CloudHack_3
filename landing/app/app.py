from flask import Flask, render_template, request, flash, redirect, url_for,jsonify
import requests
from flask_restful import Api,Resource
import json
import requests
import os



app = Flask(__name__)
api = Api(app)
app.secret_key = 'thisisjustarandomstring'


# def add(n1, n2):
#     # n1 = int(n1)
#     # n2 = int(n2)
#     # return (n1+n2)
#     return app.add(n1,n2)


def minus(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    return n1-n2

def multiply(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    return n1*n2

def divide(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    if(n2 ==0):
        return "not valid"
    return n1/n2

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    
    if number_1 =='':
        number_1 = 0
    if number_2 == '':
        number_2 = 0



    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        url = "http://addition-service:5051/add/"+str(number_1)+"/"+str(number_2)
        res = (requests.get(url).text)
        result = json.loads(res)
        result = result['result']
    elif operation == 'minus':
        url = "http://minus-service:5052/sub/"+str(number_1)+"/"+str(number_2)
        res = (requests.get(url).text)
        result = json.loads(res)
        result = result['result']
    elif operation == 'multiply':
        url = "http://multiplication-service:5053/mul/"+str(number_1)+"/"+str(number_2)
        res = (requests.get(url).text)
        result = json.loads(res)
        result = result['result']
    elif operation == 'divide':
        url = "http://division-service:5054/div/"+str(number_1)+"/"+str(number_2)
        res = (requests.get(url).text)
        result = json.loads(res)
        result = result['result']

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )