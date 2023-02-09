from sqli.data.dataview import DataView
from sqli.data.filter import Filter


class MapDataView(DataView):
    data: list[dict]

    def __init__(self, data: list[dict]) -> None:
        self.data = data
        self.cursor = 0
        # We assign ids here to better construct filters later
        for id_, d in enumerate(self.data):
            d["$id"] = id_

    def filter_by_rel(self, column_i: str, column_j: str) -> Filter:
        f = Filter()
        for record in self.data:
            f.add(record["$id"], record[column_i] == record[column_j])
        return f

    def filter_by_val(self, column: str, value: int | str) -> Filter:
        f = Filter()
        for record in self.data:
            f.add(record["$id"], record[column] == value)
        return f

    def select(self, cols: list[str] | tuple[str], filter_: Filter = None) -> DataView:
        new_data = []
        for d in self.data:
            id_ = d["$id"]
            if filter_[id_]:
                record = {k: d[k] for k in cols}
                new_data.append(record)
        return MapDataView(new_data)

    def __len__(self) -> int:
        return len(self.data)

    def __next__(self) -> int:
        if self.cursor == len(self.data):
            raise StopIteration()

        d = self.data[self.cursor]
        nk = set(d.keys()) - {"$id"}
        self.cursor += 1
        return {k: d[k] for k in nk}
