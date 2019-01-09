from flask import Blueprint, jsonify, request, abort


example = Blueprint('example', __name__)


@example.route('/')
def home():
    return jsonify('Hello')
