from lark import Lark, Transformer, v_args
from sqli.parser.grammar import sql_grammar


class CreateQueryTree(Transformer):
    @v_args(inline=True)
    def start(self, q):
        return q

    @v_args(inline=True)
    def query(self, columns, table, predicate):
        return {
            "col": columns,
            "table": table,
            "p": predicate,
        }

    @v_args(inline=True)
    def identifier(self, *args):
        print("identifier", *args)
        return str(args[0])

    @v_args(inline=True)
    def columns(self, *cols):
        return cols

    @v_args(inline=True)
    def column(self, *cols):
        return cols[0]

    @v_args(inline=True)
    def table(self, *name):
        return str(name[0])


def parse(query):
    parser = Lark(sql_grammar, parser='lalr', transformer=CreateQueryTree())
    return parser.parse(query)
