from fastapi import APIRouter
import requests
from app.services.paypal_client import get_access_token

router = APIRouter()

PAYPAL_BASE = "https://api-m.sandbox.paypal.com"


@router.post("/create-checkout-session")
def create_checkout_session(user_id: str):

    token = get_access_token()

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

    approve_url = next(
        link["href"] for link in data["links"] if link["rel"] == "approve"
    )

    return {
        "checkout_url": approve_url,
        "order_id": data["id"]
    }
