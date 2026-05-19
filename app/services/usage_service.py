from sqlalchemy.orm import Session

from app.models.usage_log import UsageLog


def log_request(
    db: Session,
    api_key_id: int,
    tenant_id: int,
    endpoint: str,
    method: str
):
    log = UsageLog(
        api_key_id=api_key_id,
        tenant_id=tenant_id,
        endpoint=endpoint,
        method=method
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log
