from flask import Flask, request
from config import SQLALCHEMY_DATABASE_URI
from models import db, ProductStock

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI

db.init_app(app)

@app.route("/stock/add", methords=['POST'])
def add_stock():
    data=request.get_json()
    product_id=data['product_id']
    quantity=data['quantity']

    stock=ProductStock.query.get(product_id)
    if stock:
        stock.quantity+=quantity
        db.session.commit(stock)
        return {'message': 'Stock created'}, 200
    else:
        stock=ProductStock(product_id=data['product_id'], quantity=data['quantity'])
        db.session.add(stock)
        db.session.commit()
        return {'message': 'Stock created'}, 201

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
