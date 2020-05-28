from src.links_utils import flat_links, map_links_to_domains


def test_map_links_to_domains():

    domains = ('google.com', 'ya.ru')

    links = (
        'https://google.com/test',
        'https://ya.ru/hello-world/test',
    )

    assert domains == map_links_to_domains(links)


def test_flat_links():

    flatten_links = (
        'https://google.com/test',
        'https://ya.ru/hello-world/test',
        'https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor',
    )

    no_flatten_linls = (
        {
            'links': (
                'https://google.com/test',
                'https://ya.ru/hello-world/test',
            )
        },
        {
            'links': (
                'https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor'
            )
        }
    )

    assert flatten_links == flat_links(no_flatten_linls)
