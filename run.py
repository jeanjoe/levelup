from flask import Flask, jsonify, request, json
from models.api import GuestList

app = Flask(__name__)
user = GuestList()

@app.route('/get-users', methods=['GET'])
def get_users():
    """Return list of all users."""
    return jsonify({ 'users': user.get_all_users() }), 200

@app.route('/add-user', methods=['POST'])
def add_user():
    """Add User to users_list."""
    data = request.get_json()
    try:
        name = data['name']
        email = data['email']
        password = data['password']
        save_user = user.add_user(name, email, password)
        if save_user == False:
            return jsonify({ "message": "This user already exists" }), 200
        return jsonify({"user": save_user, "message": "User added successfuly"}), 201
    except Exception as ex:
        return jsonify({ "error": "Field {} is required.".format(ex)})

@app.route('/delete-user/<user_name>', methods=['DELETE'])
def delete_user(user_name):
    """Delete users using name."""
    if user.delete_user(user_name):
        return jsonify({"message": "User Deleted Successfuly"}), 200
    return jsonify({ "message": "Cannot find user with username '{}'".format(user_name) }), 400

if __name__ == "__main__":
    app.run(debug=True)