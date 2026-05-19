from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from datetime import datetime

from app.db.database import Base


class UsageLog(Base):
    __tablename__ = "usage_logs"

    id = Column(Integer, primary_key=True, index=True)

    api_key_id = Column(Integer, ForeignKey("api_keys.id"), nullable=False)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=True)

    endpoint = Column(String, nullable=False)
    method = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
