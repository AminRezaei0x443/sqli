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
