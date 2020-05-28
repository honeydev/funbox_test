import inject

from src.links_utils import parse_links_json, select_unique_domains_visit


@inject.param('redis_client', 'redis_client')
async def select_visited_domains(fm, to, redis_client):
    """Select all visited domaind by given range."""
    redis = await redis_client()
    links = await redis.zrangebyscore('links', fm, to)
    parsed_links = parse_links_json(links)

    return select_unique_domains_visit(parsed_links)
