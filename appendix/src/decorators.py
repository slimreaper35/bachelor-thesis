from typing import Callable

import redis
from polars import DataFrame, read_json

from .settings import CACHE_EXPIRATION, REDIS_HOST, REDIS_PORT


def cache_in_redis(func: Callable[..., DataFrame]) -> Callable[..., DataFrame]:
    """Cache data frame in Redis."""

    def wrapper(*args, **kwargs) -> DataFrame:
        redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

        key = f"{func.__name__}:{args}:{kwargs}"
        if redis_client.exists(key):
            return read_json(redis_client.get(key))

        value = func(*args, **kwargs)
        redis_client.set(key, value.write_json(), ex=CACHE_EXPIRATION.in_seconds())
        return value

    return wrapper
