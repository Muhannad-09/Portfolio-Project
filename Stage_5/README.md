# 📘 BookBridge  
A full-stack book discovery platform built with **Flask (REST API)** and **React (Vite)**.  
BookBridge allows users to search books, view details, manage favorites, and add reviews — powered by JWT authentication and SQLAlchemy.

---

## 🚀 Features (MVP)
### 🔐 Authentication
- User registration
- Login with JWT
- Protected routes with token validation

### 🔎 Books
- Search books by title, author, or category
- View full book details

### ⭐ Favorites
- Add/remove favorites
- View user’s saved books

### 📝 Reviews
- Add and list reviews for books (MVP)

---

## 🧱 Tech Stack
**Backend**
- Python, Flask
- SQLAlchemy ORM
- JWT Authentication
- SQLite (development)

**Frontend**
- React (Vite)
- Axios
- React Router

---

## 🧪 Testing
Backend tests executed with `pytest`:


$ pytest -v
tests/test_books.py::test_list_books PASSED
tests/test_endpoints.py::test_health_books PASSED
tests/test_endpoints.py::test_register_and_login PASSED


✔ All tests passed
✔ API endpoints verified
✔ SQLite database initialized successfully

---

## ▶️ Running Locally

### Backend
```bash
cd backend
flask run

Frontend
cd frontend
npm install
npm run dev

The app will run locally with full backend–frontend integration.

| Method | Endpoint                 | Description          |
| ------ | ------------------------ | -------------------- |
| POST   | `/api/v1/auth/login`     | Login & get JWT      |
| POST   | `/api/v1/auth/register`  | Create a new account |
| GET    | `/api/v1/books`          | Search books         |
| GET    | `/api/v1/books/<id>`     | Book details         |
| POST   | `/api/v1/favorites`      | Add favorite         |
| GET    | `/api/v1/favorites`      | List favorites       |
| DELETE | `/api/v1/favorites/<id>` | Remove favorite      |

🎯 MVP Goals Achieved

Full-stack functionality delivered

Stable backend with complete test suite

Functional React client

Solid documentation and architecture

Ready for deployment and improvements

