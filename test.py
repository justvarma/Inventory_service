import unittest
import json
from app import app, db
from models import ProductStock

class InventoryServiceTestCase(unittest.TestCase):

    def setUp(self):
        # Setup test configuration
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_new_stock(self):
        response = self.client.post('/stock/add', json={
            'product_id': 1,
            'quantity': 10
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Stock created', response.data)

    def test_add_existing_stock(self):
        # Add first
        self.client.post('/stock/add', json={
            'product_id': 2,
            'quantity': 10
        })
        # Add more
        response = self.client.post('/stock/add', json={
            'product_id': 2,
            'quantity': 5
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Stock created', response.data)

    def test_remove_stock_success(self):
        self.client.post('/stock/add', json={
            'product_id': 3,
            'quantity': 10
        })
        response = self.client.post('/stock/remove', json={
            'product_id': 3,
            'quantity': 5
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Stock removed', response.data)

    def test_remove_stock_insufficient(self):
        self.client.post('/stock/add', json={
            'product_id': 4,
            'quantity': 2
        })
        response = self.client.post('/stock/remove', json={
            'product_id': 4,
            'quantity': 10
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Not enough stock', response.data)

    def test_remove_stock_not_found(self):
        response = self.client.post('/stock/remove', json={
            'product_id': 99,
            'quantity': 1
        })
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Product not found', response.data)

    def test_check_stock_found(self):
        self.client.post('/stock/add', json={
            'product_id': 5,
            'quantity': 20
        })
        response = self.client.get('/stock/check/5')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data['product_id'], 5)
        self.assertEqual(data['quantity'], 20)

    def test_check_stock_not_found(self):
        response = self.client.get('/stock/check/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Product not found', response.data)


if __name__ == '__main__':
    unittest.main()