import pytest
import inject


@pytest.fixture(autouse=True)
@inject.param('redis_client', 'redis_client')
async def drop_redis(redis_client):
    import pdb; pdb.set_trace()
    yield
    redis = await redis_client()
    await redis.flushall()
