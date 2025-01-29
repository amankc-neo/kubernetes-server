from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

cart = []

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if not product_id or not quantity:
        return jsonify({"error": "Product ID and quantity are required"}), 400

    cart_item = {"item_id": len(cart) + 1, "product_id": product_id, "quantity": quantity}
    cart.append(cart_item)
    return jsonify(cart_item), 201

@app.route('/cart/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    global cart
    cart = [item for item in cart if item["item_id"] != item_id]
    return jsonify({"message": f"Item {item_id} removed from cart"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

