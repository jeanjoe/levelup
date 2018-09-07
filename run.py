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
        save_user = user.add_user(data['name'], data['email'], data['password'])
        if not save_user:
            return jsonify({ "message": "This user already exists" }), 200
        return jsonify({"user": save_user, "message": "User added successfuly"}), 201
    except Exception as ex:
        return jsonify({ "error": "Field {} is required.".format(ex)}), 200

@app.route('/delete-user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete users using name."""
    if user.delete_user(user_id):
        return jsonify({"message": "User Deleted Successfuly"}), 200
    return jsonify({ "message": "Cannot find user with ID '{}'".format(user_id) }), 400

if __name__ == "__main__":
    app.run(debug=True)