import json
import uuid

import tldextract
from pydash import flatten


def parse_links_json(links_response):
    return tuple(map(json.loads, links_response))


def format_links_data(links):

    return json.dumps({
        **dict(links),
        'uuid': str(uuid.uuid1()),
    })


def flat_links(multiple_links):
    return tuple(
        flatten(
            list(map(
                lambda links_data: links_data['links'],
                multiple_links,
            )),
        )
    )


def map_links_to_domains(links):

    def map_method(link):
        parsed_link = tldextract.extract(link)
        return f'{parsed_link.domain}.{parsed_link.suffix}'

    return tuple(map(map_method, links))


def calc_unique_domains_visit(multiple_links):
    return set(
        map_links_to_domains(
            flat_links(multiple_links)
        )
    )
