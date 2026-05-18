from sqlalchemy import Column, Integer, String
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    # =========================
    # CORE IDENTITY
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    username = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    password = Column(
        String,
        nullable=False
    )

    # =========================
    # AUTH / SAAS ACCESS LAYER
    # =========================
    api_key = Column(
        String,
        unique=True,
        index=True,
        nullable=True
    )

    # =========================
    # USAGE / BILLING FOUNDATION
    # =========================
    request_count = Column(
        Integer,
        default=0,
        nullable=False
    )

    # 💰 READY FOR STEP 13 (BILLING)
    plan = Column(
        String,
        default="free",
        nullable=False
    )
