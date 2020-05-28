import pytest

from src.links_utils import flat_links, map_links_to_domains
from src.visited_domains_services import select_visited_domains


@pytest.mark.asyncio
async def test_insert_links(insert_links_fixture):

    inserted_domains = map_links_to_domains(flat_links(insert_links_fixture['multiple_links']))

    visited_domains = await select_visited_domains(
        insert_links_fixture['from'].timestamp(),
        insert_links_fixture['to'].timestamp(),
    )

    assert all(visited_domain in inserted_domains for visited_domain in visited_domains)
