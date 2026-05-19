from fastapi import APIRouter, Request, HTTPException

from app.db.session import SessionLocal
from app.models.user import User
from app.services.paypal_verify import verify_webhook_signature

router = APIRouter()


@router.post("/billing/paypal/webhook")
async def paypal_webhook(request: Request):

    # Parse PayPal webhook body
    body = await request.json()

    # Verify webhook signature (IMPORTANT)
    headers = request.headers

    is_valid = verify_webhook_signature(headers, body)

    if not is_valid:
        raise HTTPException(
            status_code=400,
            detail="Invalid PayPal signature"
        )

    # Get PayPal event type
    event_type = body.get("event_type")

    # Handle successful checkout approval
    if event_type == "CHECKOUT.ORDER.APPROVED":

        # Safely extract user ID from PayPal payload
        try:
            purchase_units = body["resource"].get("purchase_units", [])

            if not purchase_units:
                raise HTTPException(
                    status_code=400,
                    detail="Missing purchase units"
                )

            user_id = purchase_units[0].get("custom_id")

        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid webhook payload"
            )

        # Validate custom_id exists
        if not user_id:
            return {
                "status": "missing_user_id"
            }

        db = SessionLocal()

        try:
            # Find user in database
            user = db.query(User).filter(
                User.id == user_id
            ).first()

            if not user:
                return {
                    "status": "user_not_found"
                }

            # Idempotency guard
            # Prevent duplicate upgrades if PayPal retries webhook
            if user.plan == "pro":
                return {
                    "status": "already_upgraded"
                }

            # Upgrade SaaS plan
            user.plan = "pro"
            user.usage_limit = 10000
            user.usage_count = 0

            db.commit()

            return {
                "status": "user_upgraded"
            }

        finally:
            db.close()

    # Ignore unrelated webhook events
    return {
        "status": "ignored_event"
    }
