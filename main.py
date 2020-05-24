from http import HTTPStatus
from typing import Dict

from fastapi import FastAPI

from src.request_models import Links
from src.visited_links_services import insert_links

app = FastAPI()


@app.post('/visited_links/', status_code=HTTPStatus.CREATED)
async def add_visited_links(links: Links) -> Dict[str, str]:
    await insert_links(links)
    return {'status': 'ok'}


import src.init.di
