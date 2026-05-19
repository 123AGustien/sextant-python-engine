from fastapi import APIRouter
import requests
from app.services.paypal_client import get_access_token

router = APIRouter()

# PayPal sandbox base URL (switch to live in production)
PAYPAL_BASE = "https://api-m.sandbox.paypal.com"


@router.post("/create-checkout-session")
def create_checkout_session(user_id: str):
    """
    Create a PayPal checkout session and return approval URL.
    This is the entry point for SaaS payments.
    """

    # 1. Get PayPal OAuth access token
    token = get_access_token()

    # 2. Create PayPal order
    res = requests.post(
        f"{PAYPAL_BASE}/v2/checkout/orders",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json={
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": "10.00"
                    },
                    # Used later in webhook to identify user
                    "custom_id": user_id
                }
            ],
            "application_context": {
                "return_url": "https://your-site.com/success",
                "cancel_url": "https://your-site.com/cancel"
            }
        }
    )

    data = res.json()

    # 3. Extract approval URL (where user pays)
    approve_url = next(
        link["href"] for link in data["links"] if link["rel"] == "approve"
    )

    # 4. Return checkout session info to frontend
    return {
        "checkout_url": approve_url,
        "order_id": data["id"]
    }
