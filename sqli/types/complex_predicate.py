from enum import Enum, auto

from sqli.data.base.dataview import DataView
from sqli.types.predicate import Predicate


class ComplexPredicateType(Enum):
    AND = auto()
    OR = auto()
    NOT = auto()

    def __repr__(self) -> str:
        return self.name


class ComplexPredicate(Predicate):
    def __init__(self, type_: ComplexPredicateType, p1: Predicate, p2: Predicate) -> None:
        self.type_ = type_
        self.p1 = p1
        self.p2 = p2

    def filter(self, view: DataView):
        match self.type_:
            case ComplexPredicateType.AND:
                f1 = self.p1.filter(view)
                f2 = self.p2.filter(view)
                return f1 & f2
            case ComplexPredicateType.OR:
                f1 = self.p1.filter(view)
                f2 = self.p2.filter(view)
                return f1 | f2
            case ComplexPredicateType.NOT:
                f1 = self.p1.filter(view)
                return ~f1
            case _:
                raise RuntimeError("Unsupported simple predicate!")

    def __to_dict__(self):
        return {
            "type": repr(self.type_),
            "p1": self.p1.__to_dict__(),
            "p2": self.p2.__to_dict__() if self.p2 else "None",
        }
