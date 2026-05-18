import secrets
import hashlib


def generate_api_key() -> str:
    """
    Generate a secure API key (visible to user only once)
    """
    return "sk_" + secrets.token_urlsafe(32)


def hash_api_key(api_key: str) -> str:
    """
    Store only hashed version in DB (security best practice)
    """
    return hashlib.sha256(api_key.encode()).hexdigest()


def verify_api_key(api_key: str, stored_hash: str) -> bool:
    """
    Validate incoming API key against stored hash
    """
    return hashlib.sha256(api_key.encode()).hexdigest() == stored_hash
