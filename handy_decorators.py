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


def entry_exit(func):
    """Print when entering and exiting function."""
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        print(f"Calling {func.__name__}")
        try:
            return func(*args, **kwargs)
        finally:
            print(f"Finished calling {func.__name__}")

    return inner_func

