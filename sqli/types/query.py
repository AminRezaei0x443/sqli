from sqli.data.base.datasource import DataSource
from sqli.data.base.dataview import DataView
from sqli.types.predicate import Predicate


class Query:
    targets: list[str]
    table: str
    predicate: Predicate

    def __init__(self, targets: list[str], table: str, predicate: Predicate) -> None:
        self.targets = targets
        self.table = table
        self.predicate = predicate

    def __to_dict__(self):
        return {
            "targets": self.targets,
            "table": self.table,
            "predicate": self.predicate.__to_dict__(),
        }

    def execute(self, datasource: DataSource) -> DataView:
        # TODO: Validate query against the datasource structure before execution
        view = datasource[self.table]
        f = self.predicate.filter(view)
        return view.select(self.targets, f)
