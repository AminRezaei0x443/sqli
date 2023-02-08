from abc import ABC, abstractmethod
from enum import Enum, auto


class Predicate(ABC):
    @abstractmethod
    def filter(self, *args):
        return True


class SimplePredicateType(Enum):
    ColumnToValue = auto()
    ColumnToColumn = auto()

    def __repr__(self) -> str:
        return self.name


class ComplexPredicateType(Enum):
    AND = auto()
    OR = auto()
    NOT = auto()

    def __repr__(self) -> str:
        return self.name


class SimplePredicate(Predicate):
    def __init__(self, type_: SimplePredicateType, op1: str, op2: str) -> None:
        self.type = type_
        self.op1 = op1
        self.op2 = op2

    def filter(self, *args):
        return super().filter(*args)


class ComplexPredicate(Predicate):
    def __init__(self, type_: ComplexPredicateType, p1: Predicate, p2: Predicate) -> None:
        self.type = type_
        self.p1 = p1
        self.p2 = p2

    def filter(self, *args):
        return super().filter(*args)
