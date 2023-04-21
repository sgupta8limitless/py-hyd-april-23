import json
from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})

@app.route('/<int:id>')
def show(id):
    print(id)
    return jsonify({"message":"Hello"})


@app.route('/create',methods=['POST'])
def createData():
    print(json.loads(request.data))
    return jsonify({"message":"Hello"}),201







app.run()