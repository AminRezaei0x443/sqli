from abc import ABC, abstractmethod

from sqli.data.dataview import DataView


class Predicate(ABC):
    @abstractmethod
    def filter(self, view: DataView):
        return True
