import time
from functools import wraps
from asyncio import iscoroutinefunction


def timer(func):
    if iscoroutinefunction(func):

        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = await func(*args, **kwargs)
            runtime = (time.perf_counter() - start_time) * 1000
            print(f'Function {func.__name__} ran in {runtime} seconds.')
            return result

    else:

        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            runtime = (time.perf_counter() - start_time) * 1000
            print(f'Function {func.__name__} ran in {runtime} seconds.')
            return result

    return wrapper
