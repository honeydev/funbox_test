import json
import uuid
from typing import Dict, List, Set, Tuple

import tldextract
from pydash import flatten


def parse_links_json(links_response: List[bytes]) -> Tuple[dict, ...]:
    """Parse given from redis response jsons list."""
    return tuple(map(json.loads, links_response))


def format_links_data(links: Dict):
    """Format given links for store in redis."""
    return json.dumps({
        **dict(links),
        'uuid': str(uuid.uuid1()),
    })


def flat_links(multiple_links: Tuple[dict, ...]) -> Tuple[str, ...]:
    """Flat links in tuple."""
    return tuple(
        flatten(
            list(map(
                lambda links_data: links_data['links'],
                multiple_links,
            )),
        ),
    )


def map_links_to_domains(links: Tuple[str, ...]) -> Tuple[str, ...]:
    """Select domain name from links."""
    def map_method(link):
        parsed_link = tldextract.extract(link)
        return f'{parsed_link.domain}.{parsed_link.suffix}'

    return tuple(map(map_method, links))


def select_unique_domains_visit(multiple_links: Tuple[Dict]) -> Set[str]:
    """Select unique domains from given links."""
    return set(
        map_links_to_domains(
            flat_links(multiple_links),
        ),
    )
