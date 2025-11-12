# 📘 BookBridge – Stage 4 Report (Simple Web Client)

## 🧱 Project Overview
BookBridge is a full-stack portfolio project developed as part of Holberton School Stage 4: *MVP Execution and Web Client*.  
It connects a Flask backend (REST API with JWT authentication) to a React frontend (Vite), allowing users to search books, register/login, and manage favorites and reviews.

---

## 🚀 Sprint Planning and Execution

| Sprint | Goal | Key Tasks | Outcome |
|--------|------|-----------|----------|
| **Sprint 1** | Backend setup | Create Flask API, models, and JWT auth | Working backend with `/auth`, `/books`, `/reviews` |
| **Sprint 2** | Frontend integration | Build React UI and connect Axios APIs | Frontend successfully calls backend endpoints |
| **Sprint 3** | Stabilization | Debug, cleanup, test connectivity | Stable full-stack app running locally |

---

## 🔍 QA and Testing
- Manual testing done via `curl` and browser (e.g. `/api/v1/books/`)
- Automated testing implemented in `backend/tests/test_endpoints.py`
- Test Results: ✅ all tests passed  
- Database: SQLite (`bookbridge.db`)

$ pytest -v
============================= test session starts =============================
platform win32 -- Python 3.13.1, pytest-9.0.0, pluggy-1.6.0 --
cachedir: .pytest_cache
rootdir: Portfolio-Project\Stage_4\BookBridge\backend
plugins: anyio-4.8.0
collecting ... collected 3 items

tests/test_books.py::test_list_books PASSED                              [ 33%]
tests/test_endpoints.py::test_health_books PASSED                        [ 66%]
tests/test_endpoints.py::test_register_and_login PASSED                  [100%]

---

## 🔧 Source Repository
- **GitHub:**[https://github.com/Muhannad-09/Portfolio-Project]
- **Branch:** `main`
- All commits tracked using Git; backup copies excluded via `.gitignore`.

---

## 🧠 Sprint Reviews and Retrospectives
### Sprint Reviews
- **Sprint 1:** Backend working; database and JWT functional.
- **Sprint 2:** Frontend integration successful.
- **Sprint 3:** End-to-end tested; UI stable.

### Retrospective
- Backend and frontend integration smooth after structure cleanup.
- Major improvement needed: enhanced UI layout and responsive design.

---

## 🧰 Production / Deployment
- Runs locally on Flask + React (Vite)
- To start:
  ```bash
  # Backend
  cd backend && flask run

  # Frontend
  cd frontend && npm run dev
