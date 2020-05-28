import json

import inject
import pytest

from src.visited_links_services import insert_links


@pytest.mark.asyncio
async def test_insert_links():

    links = {
        'links': [
            'testlink1.com',
            'testlink2.com',
        ],
    }

    creation_timestamp = await insert_links(links)
    redis = await inject.instance('redis_client')()
    notes = await redis.zrangebyscore('links', creation_timestamp)

    assert 1 == len(notes)

    added_note = notes[0]
    note_links = json.loads(added_note)['links']

    assert note_links == links['links']
