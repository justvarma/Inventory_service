---

# 📦 Flask Stock Management API

A simple RESTful API built with **Flask** for managing product stock quantities. The application supports **adding**, **removing**, and **checking stock** for products using **PostgreSQL** and **Flask-SQLAlchemy**. It also features **interactive Swagger UI documentation** via **Flasgger**.

---

## 🚀 Features

* **Add Stock:** Create or update product stock quantities.
* **Remove Stock:** Safely reduce stock with validation.
* **Check Stock:** View the current stock level for any product.
* **Database:** PostgreSQL for persistent storage.
* **ORM:** SQLAlchemy for interacting with the database.
* **API Docs:** Swagger UI for live API testing.
* **Logging:** Basic logging for monitoring and debugging.
* **Environment Config:** Secure `.env` file usage.

---

## 🛠️ Tech Stack

| Tool             | Purpose                    |
| ---------------- | -------------------------- |
| Python 3.8+      | Programming Language       |
| Flask            | Web Framework              |
| Flask-SQLAlchemy | ORM for PostgreSQL         |
| Flasgger         | Swagger Documentation      |
| PostgreSQL       | Relational Database        |
| python-dotenv    | Load environment variables |

---

## 📁 Project Structure

```
flask-stock-management/
│
├── app.py              # Main Flask app with API endpoints
├── config.py           # Configuration for environment & DB
├── models.py           # SQLAlchemy model (ProductStock)
├── requirements.txt    # Python dependencies
├── .env.example        # Sample environment config
├── README.md           # Project documentation
└── migrations/         # Flask-Migrate files (optional)
```

---

## ✅ Prerequisites

* Python 3.8 or higher
* PostgreSQL installed and running
* `pip` and `git` installed

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shamshi-piserve/internship-inventory-service.git
cd internship-inventory-service

```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL

```bash
psql -U postgres
CREATE DATABASE inventory_db;
\q
```

### 5. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and update it with your PostgreSQL credentials:

```env
DB_USER=postgres
DB_PASS=your_secure_password
DB_HOST=localhost
DB_NAME=inventory_db
DB_PORT=5432
```

### 6. Initialize the Database

#### Option A: Without Flask-Migrate

```bash
python app.py
```

#### Option B: Using Flask-Migrate

```bash
flask db init
flask db migrate
flask db upgrade
```

### 7. Run the Application

```bash
python app.py
```

> 🌐 API Base URL: `http://localhost:5000`
> 📘 Swagger UI: `http://localhost:5000/apidocs`

---

## 📡 API Endpoints

| Method | Endpoint            | Description                  |
| ------ | ------------------- | ---------------------------- |
| POST   | `/stock/add`        | Add stock for a product      |
| POST   | `/stock/remove`     | Remove stock from a product  |
| GET    | `/stock/check/<id>` | Check current stock quantity |

---

## 📬 Example API Requests

### ✅ Add Stock

```bash
curl -X POST http://localhost:5000/stock/add \
-H "Content-Type: application/json" \
-d '{"product_id": 101, "quantity": 5}'
```

**Response:**

```json
{ "message": "Stock created" }
```

---

### ❌ Remove Stock

```bash
curl -X POST http://localhost:5000/stock/remove \
-H "Content-Type: application/json" \
-d '{"product_id": 101, "quantity": 2}'
```

**Response:**

```json
{ "message": "Stock removed" }
```

---

### 📊 Check Stock

```bash
curl http://localhost:5000/stock/check/101
```

**Response:**

```json
{
  "product_id": 101,
  "quantity": 3
}
```

---

## 🧪 Testing

Install testing tools:

```bash
pip install pytest pytest-flask
```

Create your tests in a `tests/` folder and run:

```bash
pytest
```

---

## 🧾 Database Schema

**Table: `product_stock`**

| Column      | Type    | Constraints               |
| ----------- | ------- | ------------------------- |
| product\_id | Integer | Primary Key               |
| quantity    | Integer | Not Null, Default: 0, ≥ 0 |

---

## 🤝 Contributing

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to GitHub: `git push origin feature/your-feature`
5. Open a Pull Request 🚀

---
