
import aioredis

from settings import Settings

settings = Settings()


async def get_redis_connection():

    if settings.test_env:
        return await aioredis.create_redis_pool('redis://localhost:6382')
    else:
        return await aioredis.create_redis_pool('redis://localhost:6381')
