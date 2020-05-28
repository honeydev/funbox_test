import os

import aioredis

from settings import Settings

settings = Settings()


async def get_redis_connection():
    """Configure redis client."""
    if settings.test_env:
        return await aioredis.create_redis_pool('redis://localhost:6382')

    return await aioredis.create_redis_pool(os.getenv('REDISCLOUD_URL'))
