from flask import Flask, jsonify
from models.api import User

app = Flask(__name__)

@app.route('/get-users', methods=['GET'])
def get_users():
    user = User()
    return jsonify({ "users": user.search_user("man")})

@app.route('/add-user', methods=['POST'])
def add_user():
    user = User()
    return jsonify({"user": user.add_user("Manzede", "manzede@gmail.com", "12345")})

@app.route('/delete-user/<user_name>', methods=['GET'])
def delete_user(user_name):
    user = User()
    if user.delete_user(user_name):
        return jsonify({"message": "User Deleted Successfuly", "users": user.get_all_users() })
    return jsonify({ "message": "Cannot find user with username '{}'".format(user_name) })


if __name__ == "__main__":
    app.run(debug=True)