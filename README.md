Flask Stock Management API
A simple RESTful API built with Flask for managing product stock quantities. The application supports adding, removing, and checking stock for products, using PostgreSQL as the database and Flask-SQLAlchemy for ORM. It includes Swagger documentation via Flasgger for easy API exploration.
Features

Add Stock: Create or update stock quantities for a product.
Remove Stock: Decrease stock quantities with validation for sufficient stock.
Check Stock: Retrieve the current stock quantity for a product.
Database: PostgreSQL for persistent storage.
ORM: Flask-SQLAlchemy for database interactions.
API Documentation: Swagger UI for interactive endpoint documentation.
Logging: Basic logging for debugging and monitoring.
Environment Configuration: Uses .env files for secure configuration.

Tech Stack

Python: 3.8+
Flask: Web framework for building the API.
Flask-SQLAlchemy: ORM for PostgreSQL integration.
Flasgger: Swagger documentation for API endpoints.
PostgreSQL: Database for storing stock data.
python-dotenv: For loading environment variables.

Project Structure
flask-stock-management/
│
├── app.py                  # Main Flask application with API endpoints
├── config.py               # Database configuration and environment variables
├── models.py               # SQLAlchemy model for ProductStock
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variable file
├── README.md               # Project documentation
└── migrations/             # Flask-Migrate database migrations (if used)

Prerequisites

Python: 3.8 or higher
PostgreSQL: Installed and running
pip: Python package manager
Git: For cloning the repository

Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-username>/flask-stock-management.git
cd flask-stock-management

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Set Up PostgreSQL

Ensure PostgreSQL is installed and running.
Create a database named inventory_db:psql -U postgres
CREATE DATABASE inventory_db;
\q



5. Configure Environment Variables

Copy the .env.example file to .env:cp .env.example .env


Edit .env with your PostgreSQL credentials:DB_USER=postgres
DB_PASS=your_secure_password
DB_HOST=localhost
DB_NAME=inventory_db
DB_PORT=5432



6. Initialize the Database

Run the Flask app to create the product_stock table:python app.py


Alternatively, if using Flask-Migrate:flask db init
flask db migrate
flask db upgrade



7. Run the Application
python app.py

The API will be available at http://localhost:5000. Access the Swagger UI at http://localhost:5000/apidocs.
API Endpoints



Method
Endpoint
Description



POST
/stock/add
Add stock to a product


POST
/stock/remove
Remove stock from a product


GET
/stock/check/<product_id>
Check stock quantity for a product


Example Requests
Add Stock
curl -X POST http://localhost:5000/stock/add \
-H "Content-Type: application/json" \
-d '{"product_id": 101, "quantity": 5}'

Response (new stock):
{
  "message": "Stock created"
}

Remove Stock
curl -X POST http://localhost:5000/stock/remove \
-H "Content-Type: application/json" \
-d '{"product_id": 101, "quantity": 2}'

Response:
{
  "message": "Stock removed"
}

Check Stock
curl http://localhost:5000/stock/check/101

Response:
{
  "product_id": 101,
  "quantity": 3
}

Swagger Documentation

Access the interactive API documentation at http://localhost:5000/apidocs.
The Swagger UI provides detailed information on request/response formats, parameters, and status codes.

Database Schema
Table: product_stock



Column
Type
Constraints



product_id
Integer
Primary Key


quantity
Integer
Not Null, Default: 0, >= 0


Testing

Install testing dependencies:pip install pytest pytest-flask


Write unit tests in a tests/ directory and run:pytest



Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.
