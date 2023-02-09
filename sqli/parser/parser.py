from lark import Lark, Transformer, v_args

from sqli.parser.grammar import sql_grammar
from sqli.types.complex_predicate import ComplexPredicate, ComplexPredicateType
from sqli.types.query import Query
from sqli.types.simple_predicate import SimplePredicate, SimplePredicateType


class CreateQueryTree(Transformer):
    @v_args(inline=True)
    def NUMBER(self, n):
        return int(n)

    @v_args(inline=True)
    def STRING(self, s):
        return str(s)[1:-1]

    @v_args(inline=True)
    def start(self, q):
        return q

    @v_args(inline=True)
    def query(self, columns, table, predicate):
        return Query(list(columns), table, predicate)

    @v_args(inline=True)
    def identifier(self, *args):
        return str(args[0])

    @v_args(inline=True)
    def columns(self, *cols):
        return cols

    @v_args(inline=True)
    def value(self, val):
        return val

    @v_args(inline=True)
    def column(self, *cols):
        return cols[0]

    @v_args(inline=True)
    def table(self, *name):
        return str(name[0])

    @v_args(inline=True)
    def column_eq(self, column_i, column_j):
        return SimplePredicate(
            SimplePredicateType.ColumnToColumn,
            column_i,
            column_j,
        )

    @v_args(inline=True)
    def column_cond(self, column, value):
        return SimplePredicate(
            SimplePredicateType.ColumnToValue,
            column,
            value,
        )

    @v_args(inline=True)
    def and_predicate(self, predicate_i, predicate_j):
        return ComplexPredicate(
            ComplexPredicateType.AND,
            predicate_i,
            predicate_j,
        )

    @v_args(inline=True)
    def or_predicate(self, predicate_i, predicate_j):
        return ComplexPredicate(
            ComplexPredicateType.OR,
            predicate_i,
            predicate_j,
        )

    @v_args(inline=True)
    def not_predicate(self, predicate):
        return ComplexPredicate(
            ComplexPredicateType.NOT,
            predicate,
            None,
        )


def parse(query) -> Query:
    parser = Lark(sql_grammar, parser="lalr", transformer=CreateQueryTree())
    return parser.parse(query)
