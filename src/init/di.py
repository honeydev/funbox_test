import inject

from src.init.redis import get_redis_connection

inject.configure(lambda binder: binder.bind('redis_client', get_redis_connection))
