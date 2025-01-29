from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

orders = []

@app.route('/order', methods=['POST'])
def place_order():
    data = request.json

    user_id = data.get("user_id")
    cart_items = data.get("cart_items")

    if not user_id or not cart_items:
        return jsonify({"error": "User ID and cart items are required"}), 400

    if not isinstance(cart_items, list):
        return jsonify({"error": "cart_items should be a list"}), 400
    
    order = {"order_id": len(orders) + 1, "user_id": user_id, "cart_items": cart_items}
    orders.append(order)
    
    return jsonify(order), 201

@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((o for o in orders if o["order_id"] == order_id), None)
    if order:
        return jsonify(order)
    
    return jsonify({"error": "Order not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
