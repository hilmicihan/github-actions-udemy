from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for testing
data = {
    'users': [
        {'id': 1, 'name': 'John Doe', 'age': 30},
        {'id': 2, 'name': 'Jane Smith', 'age': 25},
        {'id': 3, 'name': 'Bob Johnson', 'age': 40}
    ]
}

# Endpoint to get all users
@app.route('/api/users')
def get_users():
    return jsonify(data['users'])

# Endpoint to get a specific user by ID
@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    user = next((u for u in data['users'] if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# Endpoint to add a new user
@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.json
    new_user['id'] = max(u['id'] for u in data['users']) + 1
    data['users'].append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
