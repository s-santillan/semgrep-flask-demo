from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def reflect():
    data = request.get_json()["data"]
    return jsonify(data)
