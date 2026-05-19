import secrets
import hashlib


# ---------------------------
# GENERATE API KEY (ONE-TIME DISPLAY)
# ---------------------------
def generate_api_key() -> str:
    """
    Generate a secure API key.
    This is shown to the user only once.
    """
    return f"sk_{secrets.token_urlsafe(32)}"


# ---------------------------
# HASH API KEY (STORE ONLY THIS IN DB)
# ---------------------------
def hash_api_key(api_key: str) -> str:
    """
    Hash API key for secure storage in database.
    """
    if not api_key:
        raise ValueError("API key cannot be empty")

    return hashlib.sha256(api_key.encode("utf-8")).hexdigest()


# ---------------------------
# VERIFY API KEY (INCOMING REQUESTS)
# ---------------------------
def verify_api_key(api_key: str, stored_hash: str) -> bool:
    """
    Verify incoming API key against stored hash.
    """
    if not api_key or not stored_hash:
        return False

    return hashlib.sha256(api_key.encode("utf-8")).hexdigest() == stored_hash
