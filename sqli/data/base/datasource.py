from abc import ABC, abstractmethod

from sqli.data.base.dataview import DataView


class DataSource(ABC):
    @abstractmethod
    def view(self, table: str) -> DataView:
        pass

    def __getitem__(self, table: str) -> DataView:
        return self.view(table)
