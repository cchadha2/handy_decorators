import functools

from time import perf_counter


def timer(func):
    """A basic timer function decorator."""
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f'Time taken: {perf_counter() - start} seconds')

    return inner_func

