from app.db.database import SessionLocal
from app.services.usage_service import log_request


async def usage_middleware(request, call_next):
    response = await call_next(request)

    # Skip system routes
    if request.url.path in ["/", "/docs", "/openapi.json"]:
        return response

    db = SessionLocal()

    try:
        api_key_id = getattr(request.state, "api_key_id", None)
        tenant_id = getattr(request.state, "tenant_id", None)

        if api_key_id:
            log_request(
                db=db,
                api_key_id=api_key_id,
                tenant_id=tenant_id,
                endpoint=str(request.url.path),
                method=request.method
            )

    finally:
        db.close()

    return response
