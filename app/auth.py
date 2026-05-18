from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

# password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# secret key (for demo only)
SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"


# hash password
def hash_password(password: str):
    return pwd_context.hash(password)


# verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# create JWT token
def create_access_token(data: dict, expires_minutes: int = 30):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
