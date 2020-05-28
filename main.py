from http import HTTPStatus
from typing import Dict

from fastapi import FastAPI

from src.init import di
from src.request_models import Links
from src.response_models import (
    AddVisitedLinksResponse,
    GetVisitedDomainsResponse,
)
from src.visited_domains_services import select_visited_domains
from src.visited_links_services import insert_links

app = FastAPI()


@app.post('/visited_links', status_code=HTTPStatus.CREATED, response_model=AddVisitedLinksResponse)
async def add_visited_links(links: Links) -> Dict[str, str]:
    insert_timestamp = await insert_links(links)

    return {
        'status': 'ok',
        'insert_timestamp': insert_timestamp,
    }


@app.get('/visited_domains', response_model=GetVisitedDomainsResponse)
async def get_visited_domains(fm: float, to: float) -> Dict[str, str]:
    return {
        'status': 'ok',
        'domains': await select_visited_domains(fm, to)
    }
