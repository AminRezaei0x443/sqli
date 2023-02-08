from enum import Enum, auto
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

    def filter(self, *args):
        return super().filter(*args)

    def __to_dict__(self):
        return {
            "type": repr(self.type_),
            "p1": self.p1.__to_dict__(),
            "p2": self.p2.__to_dict__() if self.p2 else "None",
        }
