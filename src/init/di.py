import inject

from src.init.redis import get_redis_connection


def configure_redis(binder):
    binder.bind('redis_client', get_redis_connection)


inject.configure(configure_redis)
