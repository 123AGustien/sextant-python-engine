@router.post("/billing/paypal/webhook")
async def paypal_webhook(request: Request):

    body = await request.json()
    event_type = body.get("event_type")

    if event_type == "CHECKOUT.ORDER.APPROVED":

        # safer extraction
        try:
            purchase_units = body["resource"].get("purchase_units", [])
            user_id = purchase_units[0].get("custom_id")
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid webhook payload")

        if not user_id:
            return {"status": "missing_user_id"}

        db = SessionLocal()

        try:
            user = db.query(User).filter(User.id == user_id).first()

            if not user:
                return {"status": "user_not_found"}

            # 🔐 IDENTITY GUARD (IMPORTANT FIX)
            if user.plan == "pro":
                return {"status": "already_upgraded"}

            user.plan = "pro"
            user.usage_limit = 10000
            user.usage_count = 0

            db.commit()

            return {"status": "user_upgraded"}

        finally:
            db.close()

    return {"status": "ignored_event"}
