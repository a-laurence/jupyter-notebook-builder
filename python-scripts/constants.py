import functools
from enum import Enum


@functools.total_ordering
class ValueOrderedEnum(Enum):
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
