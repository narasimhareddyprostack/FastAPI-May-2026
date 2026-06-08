# FastAPI Employee CRUD Application - MySQL Version

This is a FastAPI application for managing employee records using MySQL database.

## Project Structure

```
crud-mysql/
├── config/
│   ├── __init__.py
│   └── database.py          # MySQL connection & configuration
├── model/
│   └── Employee.py          # SQLAlchemy ORM Model & Pydantic Schema
├── routes/
│   ├── __init__.py
│   └── emprouter.py         # Employee API endpoints
├── app.py                   # Main FastAPI application
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Setup Instructions

### 1. MySQL Database Setup

Create the MySQL database first:

```sql
CREATE DATABASE dbcrud;
```

The `employees` table will be created automatically when the application starts.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Configuration

The MySQL credentials are configured in `config/database.py`:
- **Host**: localhost
- **Port**: 3306
- **Database**: dbcrud
- **Username**: root
- **Password**: root

You can modify these credentials in `config/database.py` if needed.

### 4. Run the Application

```bash
uvicorn app:app --reload
```

The application will start at `http://127.0.0.1:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Application root |
| POST | `/emp/create` | Create new employee |
| GET | `/emp/read` | Get all employees |
| GET | `/emp/{eid}` | Get employee by ID |
| PUT | `/emp/{eid}` | Update employee |
| DELETE | `/emp/{eid}` | Delete employee |

## Request/Response Examples

### Create Employee
```bash
curl -X POST "http://127.0.0.1:8000/emp/create" \
  -H "Content-Type: application/json" \
  -d '{"eid": 101, "ename": "John", "esal": 50000, "loc": "NYC"}'
```

### Get All Employees
```bash
curl "http://127.0.0.1:8000/emp/read"
```

### Get Employee by ID
```bash
curl "http://127.0.0.1:8000/emp/101"
```

### Update Employee
```bash
curl -X PUT "http://127.0.0.1:8000/emp/101" \
  -H "Content-Type: application/json" \
  -d '{"eid": 101, "ename": "Jane", "esal": 60000, "loc": "LA"}'
```

### Delete Employee
```bash
curl -X DELETE "http://127.0.0.1:8000/emp/101"
```

## Technologies Used

- **FastAPI**: Modern web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **PyMySQL**: MySQL driver for Python
- **Pydantic**: Data validation using Python type hints

## Migration from MongoDB

The application has been migrated from MongoDB to MySQL:
- Removed PyMongo dependency
- Added SQLAlchemy ORM models
- Replaced document queries with SQL queries
- Added proper database configuration management
- All CRUD operations now use MySQL instead of MongoDB
