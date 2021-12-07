import functools

@functools.lru_cache(2048)
def seq_sum(count):
    return .5 * count * (count + 1)