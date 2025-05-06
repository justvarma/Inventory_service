from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProductStock(db.Model):
    __tablename__='product_stock'
    product_id=db.Column(db.Integer, primary_key=True)
    quantity=db.Column(db.Integer, nullable=False, default=0)