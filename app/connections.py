from django.conf import settings
import aioredis

redis_instance = None

async def get_redis_connection():
    global redis_instance
    if redis_instance is None:
        redis_instance = await aioredis.create_redis_pool(settings.REDIS_URL)
    return redis_instance
