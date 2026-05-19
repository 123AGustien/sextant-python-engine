from fastapi import APIRouter, Request, HTTPException
from app.db.session import SessionLocal
from app.models.user import User

router = APIRouter()


@router.post("/billing/paypal/webhook")
async def paypal_webhook(request: Request):

    body = await request.json()
    event_type = body.get("event_type")

    # 1. Handle successful payment
    if event_type == "CHECKOUT.ORDER.APPROVED":

        try:
            user_id = body["resource"]["purchase_units"][0]["custom_id"]
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid webhook payload")

        db = SessionLocal()

        try:
            # 2. Find user
            user = db.query(User).filter(User.id == user_id).first()

            if not user:
                return {"status": "user_not_found"}

            # 3. Upgrade SaaS plan
            user.plan = "pro"
            user.usage_limit = 10000
            user.usage_count = 0

            db.commit()

            return {"status": "user_upgraded"}

        finally:
            db.close()

    # 4. Ignore other events
    return {"status": "ignored_event"}
