# 🔐 Authentication System (SaaS Backend)

This document explains the authentication system used in the Sextant Python Engine SaaS backend.

It includes:
- JWT authentication
- Secure user identity validation
- Database user lookup
- Access protection for API routes

---

# 🧠 Overview

The system uses **JWT (JSON Web Tokens)** to securely authenticate users.

Each user receives a token after login, which must be sent with every request.

---

# 🔐 How Authentication Works

## Step 1 — User Login

User sends:

```http
POST /login
