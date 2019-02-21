
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/student')
def getStudent():
    student = {'name':'Muhammad', 'age' : 22 }
    return jsonify(result=student)

@app.route('/file')
def getFile():
    return send_file('test.pptx')


app.run()