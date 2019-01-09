from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def get_root():
    return jsonify({ 'lorem': 'ipsum' })


@app.route('/fail', methods=['GET'])
def get_fail():
    1 / 0 # Experim.
    return jsonify({ 'aaa': 'bbb' })


@app.route('/', methods=['POST'])
def post_root():
    print('-----------------------------')
    print(request.json)
    print('=============================')

    return jsonify({ 'dolor': 'sit amet' })


# import code; code.interact(local=dict(globals(), **locals()))
