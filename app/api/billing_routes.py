from fastapi import APIRouter
import stripe

router = APIRouter()


@router.post("/create-checkout-session")
def create_checkout_session():

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": "Pro API Access",
                },
                "unit_amount": 1000,
            },
            "quantity": 1,
        }],
        success_url="https://your-site.com/success",
        cancel_url="https://your-site.com/cancel",
    )

    return {"checkout_url": session.url}
