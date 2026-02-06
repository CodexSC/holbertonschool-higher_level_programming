#!/usr/bin/env python3


class CountedIterator:
    """An iterator wrapper that counts how many items have been iterated."""

    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self._iterator)
            self._count += 1
            return item
        except StopIteration:
            # propagate StopIteration as normal
            raise

    def get_count(self):
        """Return the number of items iterated so far."""
        return self._count
