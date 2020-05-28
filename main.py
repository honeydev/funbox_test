from http import HTTPStatus
from typing import Dict

from src.app import app
from src.request_models import AddLinks
from src.response_models import (
    AddVisitedLinksResponse,
    GetVisitedDomainsResponse,
)
from src.visited_domains_services import select_visited_domains
from src.visited_links_services import insert_links


@app.post('/visited_links', status_code=HTTPStatus.CREATED, response_model=AddVisitedLinksResponse)
async def add_visited_links(links: AddLinks) -> Dict[str, str]:
    """Insert given links, return timestamp with date of creation."""
    insert_timestamp = await insert_links(links)

    return {
        'status': 'ok',
        'insert_timestamp': insert_timestamp,
    }


@app.get('/visited_domains', response_model=GetVisitedDomainsResponse)
async def get_visited_domains(fm: float, to: float) -> Dict[str, str]:
    """Get visited domain by given timestamps range."""
    return {
        'status': 'ok',
        'domains': await select_visited_domains(fm, to),
    }
