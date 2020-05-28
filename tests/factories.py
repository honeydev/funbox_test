from faker import Faker
from faker.providers import internet


def get_url_factory():

    faker = Faker()
    faker.add_provider(internet)

    def inner():
        return faker.url()

    return inner


def create_links(links_count):
    url_factory = get_url_factory()

    return [
        {
            'links': (url_factory(), url_factory())
        }
        for _ in range(links_count)
    ]
