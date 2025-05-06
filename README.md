---

### 📦 *Inventory Service – E-Commerce Backend*

This service allows you to manage product stock in an e-commerce platform using a simple RESTful API. It is built using Flask, PostgreSQL, SQLAlchemy, and documented with Swagger UI.

---

## 🛠 Tech Stack

* *Backend*: Python 3.x, Flask
* *Database*: PostgreSQL
* *ORM*: SQLAlchemy
* *API Documentation*: Flasgger (Swagger UI)
* *Testing*: Pytest

---

## 🚀 How to Run the Server

### 1. *Clone the Repository*

bash
git clone https://github.com/shamshi-piserve/internship-inventory-service.git
cd internship-inventory-service


### 2. *Install Dependencies*

We recommend using a virtual environment:

bash
pip install -r requirements.txt


### 3. *Set up the Database*

* Make sure PostgreSQL is installed and running.

* Create the database manually (if not already done):

  sql
  CREATE DATABASE inventory_db;
  

* (Optional) Create a .env file or update config.py with your DB credentials.

### 4. *Initialize the Tables*

Run Python shell or script:

bash
python
>>> from app import db
>>> db.create_all()
>>> exit()


### 5. *Start the Server*

bash
python app.py


The API will run on http://localhost:5000

---

## 🧪 How to Test

### Run Unit Tests using Pytest:

bash
pytest


You can add your tests inside test_app.py or organize into a /tests folder.

---

## 📘 Access Swagger UI (API Docs)

After running the server, open this in your browser:

👉 [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

All endpoints will be visible there with descriptions and example inputs/outputs.

---

## 📌 Available Endpoints

| Method | Endpoint        | Description                |
| ------ | --------------- | -------------------------- |
| GET  | /             | Health check / welcome     |
| POST | /add_stock    | Add new stock entry        |
| POST | /remove_stock | Remove quantity from stock |
| GET  | /check_stock  | View current stock levels  |
