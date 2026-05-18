# 🔐 JWT Authentication Dependency (Production SaaS)

This module handles **secure user authentication** using JWT tokens and ensures only valid users can access protected API routes.

---

# 🧭 Purpose

- Validate JWT tokens from request headers
- Extract user identity safely
- Fetch user from database
- Block invalid or expired tokens

---

# 🔐 Implementation

```python id="dep_py_01"
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from app.models.user import User
from app.db.deps import get_db
from sqlalchemy.orm import Session

SECRET_KEY = "CHANGE_THIS_SECRET_KEY"
ALGORITHM = "HS256"

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
