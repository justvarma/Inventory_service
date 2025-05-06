---

# 📦 **Inventory Service – E-Commerce Backend**

This service allows you to manage product stock in an e-commerce platform using a simple RESTful API.
It is built using **Flask**, **PostgreSQL**, **SQLAlchemy**, and documented with **Swagger UI**.

---

## 🛠 Tech Stack

* **Backend**: Python 3.x, Flask
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **API Documentation**: Flasgger (Swagger UI)
* **Testing**: Pytest

---

## 🚀 How to Run the Server

### 1. Clone the Repository

```bash
git clone https://github.com/shamshi-piserve/internship-inventory-service.git
cd internship-inventory-service
```

### 2. Install Dependencies

It’s recommended to use a virtual environment:

```bash
pip install -r requirements.txt
```

### 3. Set Up the Database

* Make sure PostgreSQL is installed and running.
* Create the database manually (if not already done):

```sql
CREATE DATABASE inventory_db;
```

* *(Optional)* Create a `.env` file or update `config.py` with your DB credentials:

```env
DB_USER=postgres
DB_PASS=yourpassword
DB_HOST=localhost
DB_NAME=inventory_db
```

### 4. Initialize the Tables

Start Python shell and run:

```bash
python
```

```python
from app import db
db.create_all()
exit()
```

### 5. Start the Server

```bash
python app.py
```

Your API will now be available at:
📍 `http://localhost:5000/apidocs`

---

## 🧪 How to Test

Run unit tests using **Pytest**:

```bash
pytest
```

You can place your tests inside `test_app.py` or organize them in a `/tests` directory.

---

## 📘 Access Swagger UI (API Docs)

Once the server is running, access the Swagger UI here:
👉 [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

It provides interactive documentation for all available endpoints.

---

## 📌 Available Endpoints

| Method | Endpoint        | Description                |
| ------ | --------------- | -------------------------- |
| `GET`  | `/`             | Health check / Welcome     |
| `POST` | `/add_stock`    | Add new stock entry        |
| `POST` | `/remove_stock` | Remove quantity from stock |
| `GET`  | `/check_stock`  | View current stock levels  |

---
