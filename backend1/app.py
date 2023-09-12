from flask import Flask, request, jsonify
import requests  

app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'All fields are required'}), 400

    
    user_data = {
        'username': username,
        'email': email,
        'password': password
    }

    
    response = requests.post('http://backend2:5001/create_user', json=user_data)

    if response.status_code == 201:
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'message': 'Failed to create user'}), 
        
@app.route('/get_users', methods=['GET'])
def get_users():
    backend2_url = 'http://backend2:5001/get_users'  
    responseGet = requests.get(backend2_url)
    if responseGet.status_code == 200:
        
        user_list = responseGet.json()
        return jsonify({'message': 'User created successfully', 'users': user_list}), 201
    else:
        
        return jsonify({'message': 'Failed to retrieve user list from backend2'}), 500

    
   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)