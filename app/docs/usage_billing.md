# 💰 Step 19 — Usage Tracking & Billing System

This module introduces **real SaaS monetisation infrastructure** by tracking API usage per user and preparing data for billing.

It connects:
- API keys (Step 18)
- Rate limiting (Step 16)
- Stripe payments (Step 13–14)

---

# 🧠 Purpose

This system enables:

- Tracking API usage per request
- Logging endpoint access
- Preparing billing data per user
- Enabling pay-per-use SaaS models

Used in systems like:
- OpenAI usage-based billing
- Stripe metered billing systems

---

# 🗄️ Usage Log Database Model

### File: `app/models/usage.py`

```python
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.db.database import Base


class UsageLog(Base):
    __tablename__ = "usage_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    endpoint = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
