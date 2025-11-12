# 📘 BookBridge Documentation

## 🧱 Overview
**BookBridge** is a full-stack web application developed during **Holberton School – Stage 4: MVP Execution and Web Client**.  
It combines a **Flask (Python)** backend API with a **React (Vite)** frontend to provide a seamless platform for users to explore, share, and review books.

---

## 📂 Folder Contents
| File | Description |
|------|--------------|
| `Stage4.md` | Final project report including sprint planning, testing, and retrospective. |
| `README.md` | This documentation index file summarizing project scope and usage. |

---

## 🚀 Key Features

- **Backend:** Flask API with JWT authentication, SQLAlchemy ORM, and CORS.  
- **Frontend:** React (Vite) app using Axios for API integration.  
- **Database:** SQLite (development), easily replaceable with PostgreSQL/MySQL.  
- **Testing:** Automated tests using Pytest for endpoints and database validation.  
- **Version Control:** GitHub repository for collaboration and version tracking.

---

## 🧩 Setup Instructions

To run locally:

```bash
# Backend
cd backend
flask run

# Frontend
cd frontend
npm run dev
```
---

## 🧪 QA and Testing Summary

```All API endpoints tested with pytest:
tests/test_books.py::test_list_books PASSED
tests/test_endpoints.py::test_health_books PASSED
tests/test_endpoints.py::test_register_and_login PASSED
```
## ✅ Backend stable verified endpoints, authentication, and database integrity.

## 👥 Author

**Developed by:** *Muhannad Gsgs*
***Software Engineering
📅 2025*** 
