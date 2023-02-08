sql_grammar = """

start: query

query: "SELECT" columns "FROM" table "WHERE" predicate
columns: column ("," column)*

predicate: column "=" column -> column_eq
         | column "=" value -> column_cond
         | predicate "and" predicate -> and_predicate
         | predicate "or" predicate -> or_predicate
         | "not" predicate -> not_predicate

value: NUMBER | STRING
column: identifier
table: identifier

identifier: /[a-zA-Z_][a-zA-Z0-9_]*/

%import common.ESCAPED_STRING   -> STRING
%import common.SIGNED_NUMBER    -> NUMBER
%ignore " "

"""
