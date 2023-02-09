from sqli.data.base.datasource import DataSource
from sqli.data.base.dataview import DataView
from sqli.data.map.map_dataview import MapDataView
import json


class MapDataSource(DataSource):
    source: dict[str, list[dict]]

    def __init__(self, source: dict[str, list[dict]]) -> None:
        self.source = source

    def view(self, table: str) -> DataView:
        view = MapDataView(self.source[table])
        return view

    @classmethod
    def from_csv(self, csv_path_data: dict[str, str]) -> "MapDataSource":
        # We rely on pandas for this part
        import pandas as pd

        src = {}
        for table, file in csv_path_data.items():
            df = pd.read_csv(file)
            src[table] = df.to_dict("records")
        return MapDataSource(src)

    @classmethod
    def from_json(self, json_path: str) -> "MapDataSource":
        with open(json_path, "r") as f:
            src = json.load(f)
        return MapDataSource(src)
