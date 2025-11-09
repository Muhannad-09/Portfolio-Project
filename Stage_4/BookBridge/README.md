# 📚 BookBridge

**BookBridge** is a full-stack web application designed to connect readers, empower discovery, and encourage engagement through community-driven book reviews.  
It bridges the gap between passionate readers and a rich library of book data with user authentication, reviews, and administrative control.

---

## 🧠 Project Overview

BookBridge provides a modern, intuitive platform for exploring and reviewing books.  
Users can create accounts, browse book listings, leave reviews, and manage favorites.  
Administrators have elevated permissions to manage the catalog — adding, editing, or removing books directly through secure endpoints.

The project demonstrates **end-to-end web application development**: a RESTful Flask backend API integrated with a responsive React frontend.

---

## 🎯 Objectives

- Deliver a **clean, functional full-stack application** with authentication and CRUD features.
- Showcase **software engineering principles** — modular design, RESTful routing, and component-based UI.
- Implement **secure JWT authentication** and role-based access.
- Provide **a foundation for future scalability**, including API expansion and UI theming.

---

## 💡 Key Features

### 👤 User
- Register and log in securely with JWT authentication.
- Browse and search for books by title or category.
- Submit, edit, and delete personal reviews.
- Save favorites for quick access.

### 🧑‍💼 Admin
- Full control over book listings.
- Add new books, edit details, or delete outdated entries.
- Manage inappropriate reviews if needed.

### 📖 Books & Reviews
- Detailed book cards with cover images, author, and descriptions.
- Real-time reviews section powered by Flask REST APIs.
- Rating system (1–5 stars) and user comments.

---

## 🏗️ System Architecture

BookBridge follows a **client–server architecture**:

## 🧩 Tech Stack

### 🔙 Backend
- **Framework:** Flask  
- **Database:** SQLite (via SQLAlchemy)  
- **Auth:** JWT (JSON Web Tokens)  
- **CORS:** Flask-CORS  
- **ORM:** SQLAlchemy  
- **Migrations:** Flask-Migrate  

### 💻 Frontend
- **Framework:** React (Vite)  
- **Routing:** React Router  
- **HTTP Client:** Axios  
- **Styling:** CSS  

---

## ⚙️ Technical Highlights

| Layer | Technology | Purpose |
|-------|-------------|----------|
| Backend | Flask | API framework |
| Database | SQLAlchemy (SQLite) | Persistent storage |
| Authentication | Flask-JWT-Extended | Token-based user sessions |
| Frontend | React (Vite) | Dynamic UI and routing |
| Communication | Axios | API requests |
| Deployment | GitHub + Localhost | Development setup |

---

## 🧩 Project Structure

### 📂 Backend (`/backend`)
Handles all **API logic, authentication, and database management**.

**Key files:**
- `app/__init__.py` → Flask app factory  
- `app/models.py` → Database models (User, Book, Review)  
- `app/routes/` → REST API endpoints (auth, books, reviews)  
- `app/schemas.py` → JSON serializers for models  
- `app/utils.py` → Role-based access helpers  
- `requirements.txt` → Backend dependencies  
- `run.py` → Entry point for running the Flask server  

---

### 💻 Frontend (`/frontend`)
Handles all **user interface and client-side logic**, built with React + Vite.

**Key files:**
- `src/components/` → Reusable UI components (Navbar, BookCard, etc.)  
- `src/pages/` → Page views (Login, Register, Favorites, SearchBooks)  
- `src/services/` → API communication using Axios  
- `src/styles/` → CSS files for styling  
- `src/App.jsx` → Main application routes  
- `package.json` → Frontend dependencies  
- `vite.config.js` → Vite configuration file  

---

### 🧠 Summary
- **Backend:** Python (Flask) + SQLAlchemy + JWT  
- **Frontend:** React (Vite) + Axios + React Router  
- **Architecture:** RESTful API + Client-Server Communication  

---

## 🧭 Future Enhancements

- 🌍 Cloud deployment using AWS or Render.  
- 📊 Advanced search filters (genre, author, year).  
- ❤️ Enhanced UI/UX using Tailwind or Material UI.  
- 🧾 User profile pages with reading history and stats.

---

## 👨‍💻 Author

**Developed by:** *Muhannad Gsgs* 
**Program:** Holberton School – Portfolio Project (Stage 4)  
**Focus:** Full-Stack Software Engineering  

---
