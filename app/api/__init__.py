
from .auth_routes import router as auth_router
from .protected_routes import router as protected_router
from .admin_routes import router as admin_router
from .billing_routes import router as billing_router
from .user_routes import router as user_router
from .webhooks import router as webhooks_router

all_routers = [
    auth_router,
    protected_router,
    admin_router,
    billing_router,
    user_router,
    webhooks_router,
]
