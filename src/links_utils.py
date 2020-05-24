import uuid
import json


def format_links_data(links):

    return json.dumps({
        **dict(links),
        'uuid': str(uuid.uuid1()),
    })
