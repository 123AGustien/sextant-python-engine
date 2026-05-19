from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.database import Base


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)

    # Workspace identity
    name = Column(String, unique=True, index=True, nullable=False)

    # Ownership / linking to user system
    owner_id = Column(Integer, index=True, nullable=False)

    # Lifecycle
    created_at = Column(DateTime, default=datetime.utcnow)
