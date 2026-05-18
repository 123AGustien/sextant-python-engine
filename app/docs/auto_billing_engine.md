# 💳 Step 20 — Automatic Billing Engine (Revenue Automation)

This step converts usage tracking into **real automated billing**.

It is the final core layer of a monetised SaaS backend.

Built on top of:
- API Keys (Step 18)
- Usage Tracking (Step 19)
- Stripe Payments integration

---

# 🧠 Purpose

This system enables:

- Convert API usage → monetary value
- Generate monthly charges automatically
- Store billing records per user
- Prepare Stripe auto-charge flow

Used in systems like:
- OpenAI usage-based billing
- Stripe subscription + metered billing

---

# 💰 Billing Logic

## Example Pricing Model

| Plan | Price |
|------|------|
| Free | $0 |
| Pro | $10/month |
| Pay-per-use | $0.001 per request |

---

# 🗄️ STEP 20.1 — BILLING MODEL

### File: `app/models/billing.py`

```python id="bill_01"
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from datetime import datetime

from app.db.database import Base


class BillingRecord(Base):
    __tablename__ = "billing_records"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    total_requests = Column(Integer, default=0)

    total_cost = Column(Float, default=0.0)

    created_at = Column(DateTime, default=datetime.utcnow)
