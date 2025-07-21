from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy user data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(k in data for k in ('id', 'name', 'email')):
        return jsonify({"error": "Missing user data (id, name, or email)"}), 400
    if any(u['id'] == data['id'] for u in users):
        return jsonify({"error": "User with this ID already exists"}), 400
    users.append(data)
    return jsonify(data), 201

# PUT (update) user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.update({k: data[k] for k in data if k in user})
    return jsonify(user), 200

# DELETE user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": f"User {user_id} deleted"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
