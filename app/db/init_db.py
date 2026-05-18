from app.db.database import Base, engine

# Import all models so SQLAlchemy registers them
from app.models.user import User  # noqa: F401
from app.models.tenant import Tenant  # noqa: F401


def init_db():
    """
    Creates all database tables on startup.
    Safe for Railway + local dev.
    """
    Base.metadata.create_all(bind=engine)
