from flask import Flask, request, jsonify
from flasgger import Swagger
from config import SQLALCHEMY_DATABASE_URI
from models import db, ProductStock

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI
swagger = Swagger(app)

db.init_app(app)

@app.route('/')
def home():
    return {"message": "Inventory Service Running"}

@app.route("/stock/add", methods=['POST'])
def add_stock()::
    """
        Add stock to a product
        ---
        tags:
          - Stock Management
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - product_id
                - quantity
              properties:
                product_id:
                  type: integer
                  example: 101
                quantity:
                  type: integer
                  example: 5
        responses:
          200:
            description: Stock updated successfully
          201:
            description: New stock created successfully
          400:
            description: Invalid input
        """
    data=request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    product_id=data.get('product_id')
    quantity=data.get('quantity')

    if not product_id or quantity is None:
        return jsonify({"error": "Both product_id and quantity are required"}), 400

    stock=ProductStock.query.get(product_id)
    if stock:
        stock.quantity+=quantity
        db.session.commit()
        return jsonify({'message': 'Stock created'}), 200
    else:
        stock=ProductStock(product_id=product_id, quantity=quantity)
        db.session.add(stock)
        db.session.commit()
        return jsonify({'message': 'Stock created'}), 201

@app.route("/stock/remove", methods=['POST'])
def remove_stock():
    """
        Remove stock to a product
        ---
        tags:
          - Stock Management
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - product_id
                - quantity
              properties:
                product_id:
                  type: integer
                  example: 101
                quantity:
                  type: integer
                  example: 5
        responses:
          200:
            description: Stock removed successfully
          400:
            description: Invalid input or not enough stock
          404:
            description: Product not found
        """
    data=request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    product_id=data.get('product_id')
    quantity=data.get('quantity')

    if not product_id or quantity is None:
        return jsonify({"error": "Both product_id and quantity are required"}), 400

    stock=ProductStock.query.get(product_id)
    if stock and stock.quantity>=quantity:
        stock.quantity-=quantity
        db.session.commit()
        return jsonify({'message': 'Stock removed'}), 200
    elif stock:
        return jsonify({'error': 'Not enough stock'}), 400
    else:
        return jsonify({'error': 'Product not found'}), 404

@app.route("/stock/check/<int:product_id>", methods=['GET'])
def check_stock(product_id):
    """
        Check stock to a product
        ---
        tags:
          - Stock Management
        parameters:
          - name: product_id
            in: path
            type: integer
            required: true
            description: ID of the product
        responses:
          200:
            description: Stock quantity returned
            schema:
              type: object
              properties:
                product_id:
                  type: integer
                quantity:
                  type: integer
          404:
            description: Product not found
        """
    stock=ProductStock.query.get(product_id)
    if stock:
        return jsonify({
            "product_id": product_id,
            "quantity": stock.quantity}), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)