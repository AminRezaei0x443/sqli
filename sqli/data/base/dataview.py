from abc import ABC, abstractmethod

from sqli.data.base.filter import Filter


class DataView(ABC):
    @abstractmethod
    def filter_by_rel(self, column_i: str, column_j: str) -> Filter:
        pass

    @abstractmethod
    def filter_by_val(self, column: str, value: str | int) -> Filter:
        pass

    @abstractmethod
    def select(self, cols: list[str] | tuple[str], filter_: Filter = None) -> "DataView":
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self) -> int:
        pass
