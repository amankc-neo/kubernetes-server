from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

@app.route('/users/login', methods=['POST'])
def login_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON format"}), 400

    data = request.get_json()  
    if not data:
        return jsonify({"error": "No data provided"}), 400

    return jsonify({"message": "User authenticated successfully", "data": data}), 200

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    
    user_data = {"id": id, "name": "AmanKC-neo"}
    
   
    return jsonify(user_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
