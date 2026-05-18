# Sextant SaaS Backend Template

Production-style FastAPI backend template demonstrating scalable API architecture, authentication, modular service design, and SaaS-ready backend engineering.

---

## 🚀 Features

- FastAPI REST API
- JWT Authentication System
- User Registration & Login
- Protected Routes
- Password Hashing with bcrypt
- Modular Backend Architecture
- SQLAlchemy-ready structure
- SaaS-ready backend foundation
- GitHub Actions workflow support
- Railway / cloud deployment ready

---

## 🧱 Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn
- SQLAlchemy
- python-jose
- passlib
- bcrypt

---

## 📁 Project Structure

```text
app/
│
├── api/
│   └── auth_routes.py
│
├── core/
│   └── security.py
│
├── middleware/
│   └── auth_middleware.py
│
├── services/
│   └── auth_service.py
│
├── db/
│
├── models/
│
└── main.py

requirements.txt
runtime.txt
Procfile
README.md
LICENSE
```

---

## 🔐 Authentication Features

### Register Endpoint

```http
POST /register
```

Registers a new user account.

---

### Login Endpoint

```http
POST /login
```

Returns JWT bearer token after successful authentication.

---

### Protected Profile Endpoint

```http
GET /profile
```

Requires valid JWT bearer token.

---

## ▶️ Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend server:

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically generates Swagger API documentation.

---

## 🔑 JWT Authentication Flow

1. Register user
2. Login user
3. Receive JWT token
4. Authorize using Bearer token
5. Access protected routes

---

## 🧩 SaaS Expansion Roadmap

Planned upgrades:

- Database persistence
- PostgreSQL integration
- User roles & permissions
- API key system
- Subscription billing integration
- Stripe support
- Multi-tenant architecture
- Usage analytics
- Rate limiting

---

## 📦 Deployment Ready

Supports deployment platforms such as:

- Railway
- Render
- Docker
- VPS / Cloud VM
- Kubernetes-ready architecture

---

## 🧠 Engineering Philosophy

Designed as a reusable SaaS backend foundation with clean modular separation of concerns and scalable architecture patterns.

---

## 📄 License

MIT License

Copyright (c) 2026 Mr. Don Herman Oswald Weerasekera

---

## 👤 Author

Mr. Don Herman Oswald Weerasekera

GitHub:
[github.com](https://reference-url-citation.invalid/0)

Project Repository:
[github.com](https://reference-url-citation.invalid/1)
