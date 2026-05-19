import os
import requests
from requests.auth import HTTPBasicAuth


PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_SECRET = os.getenv("PAYPAL_SECRET")

PAYPAL_BASE = "https://api-m.sandbox.paypal.com"


def verify_webhook_signature(headers, body):

    webhook_id = os.getenv("PAYPAL_WEBHOOK_ID")

    auth = HTTPBasicAuth(
        PAYPAL_CLIENT_ID,
        PAYPAL_SECRET
    )

    access_token_res = requests.post(
        f"{PAYPAL_BASE}/v1/oauth2/token",
        auth=auth,
        data={
            "grant_type": "client_credentials"
        }
    )

    access_token = access_token_res.json()["access_token"]

    verify_res = requests.post(
        f"{PAYPAL_BASE}/v1/notifications/verify-webhook-signature",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "auth_algo": headers.get("paypal-auth-algo"),
            "cert_url": headers.get("paypal-cert-url"),
            "transmission_id": headers.get("paypal-transmission-id"),
            "transmission_sig": headers.get("paypal-transmission-sig"),
            "transmission_time": headers.get("paypal-transmission-time"),
            "webhook_id": webhook_id,
            "webhook_event": body
        }
    )

    data = verify_res.json()

    return data.get("verification_status") == "SUCCESS"
