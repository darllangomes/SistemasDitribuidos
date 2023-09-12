from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User  # Importe o modelo User do arquivo models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db/db_example'
db.init_app(app)  # Inicialize o SQLAlchemy com o aplicativo Flask

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'All fields are required'}), 400

    new_user = User(username=username, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_tables', methods=['POST'])
def create_tables():
    with app.app_context():
        db.create_all()
    return jsonify({'message': 'Tabelas criadas com sucesso'}), 200

@app.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify(user_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
