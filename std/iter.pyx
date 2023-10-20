from abc import ABC

from .option import Option
from .result import Result

class Iterator(ABC):
    type Item

    cdef Option[Item] next(self)
