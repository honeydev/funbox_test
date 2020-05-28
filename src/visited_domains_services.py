import inject

from src.links_utils import calc_unique_domains_visit, parse_links_json


@inject.param('redis_client', 'redis_client')
async def select_visited_domains(fm, to, redis_client):
    redis = await redis_client()
    links = await redis.zrangebyscore('links', fm, to)
    parsed_links = parse_links_json(links)

    return calc_unique_domains_visit(parsed_links)
