import os
import requests

PAYPAL_BASE = (
    "https://api-m.sandbox.paypal.com"
    if os.getenv("PAYPAL_MODE") == "sandbox"
    else "https://api-m.paypal.com"
)

def get_access_token():
    res = requests.post(
        f"{PAYPAL_BASE}/v1/oauth2/token",
        auth=(os.getenv("PAYPAL_CLIENT_ID"), os.getenv("PAYPAL_SECRET")),
        headers={"Accept": "application/json"},
        data={"grant_type": "client_credentials"},
    )

    return res.json()["access_token"]
