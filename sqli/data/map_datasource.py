from sqli.data.datasource import DataSource
from sqli.data.dataview import DataView
from sqli.data.map_dataview import MapDataView


class MapDataSource(DataSource):
    source: dict[str, list[dict]]

    def __init__(self, source: dict[str, list[dict]]) -> None:
        self.source = source

    def view(self, table: str) -> DataView:
        view = MapDataView(self.source[table])
        return view
