# 🧠 Redis Cache Layer (Step 23)

This module adds caching to reduce database load and improve API speed.

---

## 🧱 Cache Implementation

```python
import redis
import os

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)

def set_cache(key, value, ttl=60):
    redis_client.setex(key, ttl, value)

def get_cache(key):
    return redis_client.get(key)
