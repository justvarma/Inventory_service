from flask import Flask, request, jsonify
from config import SQLALCHEMY_DATABASE_URI
from models import db, ProductStock

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI

db.init_app(app)

@app.route("/stock/add", methods=['POST'])
def add_stock():
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

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)