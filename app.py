
from flask import Flask, request, jsonify
users = {}

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    users.setdefault(str(data["user_id"]), {"points": 0})
    return jsonify({"ok": True})

@app.route("/add_points", methods=["POST"])
def add_points():
    data = request.json
    users[str(data["user_id"])]["points"] += int(data["points"])
    return jsonify({"success": True})

@app.route("/balance/<user_id>")
def balance(user_id):
    return jsonify({"points": users.get(str(user_id), {}).get("points", 0)})

app.run(host="0.0.0.0", port=5000)
