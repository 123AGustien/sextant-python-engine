from fastapi import APIRouter, Request
import stripe
import os

router = APIRouter()

WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")


@router.post("/stripe-webhook")
async def stripe_webhook(request: Request):

    payload = await request.body()

    event = stripe.Event.construct_from(
        payload,
        stripe.api_key
    )

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        print("Payment success:", session)

    return {"status": "ok"}
