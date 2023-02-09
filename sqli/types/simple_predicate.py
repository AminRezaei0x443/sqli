from enum import Enum, auto

from sqli.data.base.dataview import DataView
from sqli.types.predicate import Predicate


class SimplePredicateType(Enum):
    ColumnToValue = auto()
    ColumnToColumn = auto()

    def __repr__(self) -> str:
        return self.name


class SimplePredicate(Predicate):
    def __init__(self, type_: SimplePredicateType, op1: str, op2: str) -> None:
        self.type_ = type_
        self.op1 = op1
        self.op2 = op2

    def filter(self, view: DataView):
        if self.type_ == SimplePredicateType.ColumnToColumn:
            return view.filter_by_rel(self.op1, self.op2)
        elif self.type_ == SimplePredicateType.ColumnToValue:
            return view.filter_by_val(self.op1, self.op2)
        else:
            raise RuntimeError("Unsupported simple predicate!")

    def __to_dict__(self):
        return {
            "type": repr(self.type_),
            "op1": self.op1,
            "op2": self.op2,
        }
