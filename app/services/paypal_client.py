import os
import requests
from requests.auth import HTTPBasicAuth

# Load from environment variables (NEVER hardcode in production)
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_SECRET = os.getenv("PAYPAL_SECRET")

# Sandbox base URL (switch to live for production)
PAYPAL_BASE = "

"def get_access_token() -> str:
    """
    Fetch OAuth access token from PayPal.
    Required for all API calls (orders, payments, etc.)
    """

    if not PAYPAL_CLIENT_ID or not PAYPAL_SECRET:
        raise Exception("Missing PayPal credentials in environment variables")

    response = requests.post(
        f"{PAYPAL_BASE}/v1/oauth2/token",
        headers={
            "Accept": "application/json",
            "Accept-Language": "en_US",
        },
        auth=HTTPBasicAuth(PAYPAL_CLIENT_ID, PAYPAL_SECRET),
        data={
            "grant_type": "client_credentials"
        }
    )

    if response.status_code != 200:
        raise Exception(f"Failed to get PayPal token: {response.text}")

    data = response.json()

    return data["access_token"]
