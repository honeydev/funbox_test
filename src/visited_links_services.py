from datetime import datetime

import inject

from src.links_utils import format_links_data


@inject.param('redis_client', 'redis_client')
async def insert_links(links, redis_client):
    """Insert given links in database."""
    redis = await redis_client()

    current_timestamp = datetime.now().timestamp()

    await redis.zadd('links', current_timestamp, format_links_data(links))

    return current_timestamp
