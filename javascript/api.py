from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"endpoints": ["all/"], "message": "you can do these actions"})


@app.route("/login", methods= ["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username == "admin" and password == "123456":
        return jsonify({"status": 200})
    else:
        return jsonify({"status": 400})


app.run(debug=True, port=5000)
