from passlib.context import CryptContext

"""
Auth Service Module
Handles password hashing and verification for SaaS authentication layer.
Production-safe implementation using bcrypt.
"""

# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash a plain text password using bcrypt.

    Args:
        password (str): Raw user password

    Returns:
        str: Hashed password string
    """
    if not password:
        raise ValueError("Password cannot be empty")

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.

    Args:
        plain_password (str): User input password
        hashed_password (str): Stored bcrypt hash

    Returns:
        bool: True if match, False otherwise
    """
    if not plain_password or not hashed_password:
        return False

    return pwd_context.verify(plain_password, hashed_password)
