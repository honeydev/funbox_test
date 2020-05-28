from datetime import datetime

import inject
import pytest

from src.visited_links_services import insert_links
from tests.factories import create_links, get_url_factory


@pytest.fixture(autouse=True)
async def clear_db():
    redis = await inject.instance('redis_client')()
    yield
    await redis.flushall()


@pytest.fixture
async def insert_links_fixture():
    time_start = datetime.now()

    multiple_links = create_links(2)

    for links in multiple_links:
        await insert_links(links)

    time_end = datetime.now()

    return {
        'from': time_start,
        'multiple_links': multiple_links,
        'to': time_end,
    }
