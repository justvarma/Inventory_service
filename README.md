```markdown
# 📦 Inventory Service – E-Commerce Backend

A lightweight REST API for real-time inventory management in e-commerce systems. Provides essential stock operations with full Swagger documentation.

---

## 🛠️ Tech Stack

| Component          | Technology               |
|--------------------|--------------------------|
| **Framework**      | Flask 3.x               |
| **Language**       | Python 3.10+            |
| **Database**       | PostgreSQL 14+          |
| **ORM**            | SQLAlchemy 2.0          |
| **API Docs**       | Flasgger (Swagger UI 3) |
| **Testing**        | Pytest                  |

---

## 🚀 Getting Started

### Prerequisites
- PostgreSQL server running
- Python 3.10+

### Installation
```bash
# Clone repository
git clone https://github.com/shamshi-piserve/internship-inventory-service.git
cd internship-inventory-service

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Database Setup
1. Create PostgreSQL database:
```sql
CREATE DATABASE inventory_db;
```

2. Configure connection in `.env`:
```ini
DATABASE_URL=postgresql://username:password@localhost:5432/inventory_db
```

3. Initialize tables:
```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

### Running the Server
```bash
# Development mode
python app.py

# Production mode (recommended):
gunicorn -w 4 -b :5000 app:app
```
→ Server runs at `http://localhost:5000`

---

## 🧪 Testing
```bash
# Run all tests
pytest -v

# Run with coverage report
pytest --cov=app --cov-report=html
```
**Test Structure**:
- Unit tests: `tests/test_models.py`
- Integration tests: `tests/test_routes.py`

---

## 📘 API Documentation
Access interactive Swagger UI at:  
🔗 [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

**Try sample requests directly in the browser!**

---

## 📌 API Endpoints

| Method | Endpoint          | Request Body                              | Description                     |
|--------|-------------------|------------------------------------------|---------------------------------|
| POST   | `/stock/add`      | `{"product_id": str, "quantity": int}`   | Add/update product stock        |
| POST   | `/stock/remove`   | `{"product_id": str, "quantity": int}`   | Reduce stock quantity           |
| GET    | `/stock/check/{id}` | -                                      | Check current stock levels      |
| GET    | `/health`         | -                                        | Service health check            |

---

## 🆘 Troubleshooting
**Common Issues:**
- **Database Connection Failed**: Verify PostgreSQL is running and credentials in `.env` are correct
- **Missing Dependencies**: Re-run `pip install -r requirements.txt`
- **Port Conflicts**: Change port with `flask run --port=5001`

```
