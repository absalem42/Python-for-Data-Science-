def ft_filter(function, iterable) -> iter:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return iter([item for item in iterable if item])
    return iter([item for item in iterable if function(item)])
