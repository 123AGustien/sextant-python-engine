from app.db.database import Base, engine

# Import all models so SQLAlchemy registers them before create_all()
from app.models.user import User  # noqa: F401
from app.models.tenant import Tenant  # noqa: F401


def init_db():
    """
    Initialize database schema.
    Safe for Railway, local dev, and repeated deployments.
    """
    Base.metadata.create_all(bind=engine)
