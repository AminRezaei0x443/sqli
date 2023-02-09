from abc import ABC, abstractmethod

from sqli.data.base.dataview import DataView


class Predicate(ABC):
    @abstractmethod
    def filter(self, view: DataView):
        return True
