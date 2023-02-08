from sqli.parser.parser import parse


def test_parser_1():
    query = "SELECT id, name FROM students WHERE id=1"
    r = parse(query)
    assert r.__to_dict__() == {
        "targets": [
            "id",
            "name",
        ],
        "table": "students",
        "predicate": {
            "type": "ColumnToValue",
            "op1": "id",
            "op2": 1,
        },
    }


def test_parser_2():
    query = 'SELECT id, name FROM students WHERE id="1"'
    r = parse(query)
    assert r.__to_dict__() == {
        "targets": [
            "id",
            "name",
        ],
        "table": "students",
        "predicate": {
            "type": "ColumnToValue",
            "op1": "id",
            "op2": "\"1\"",
        },
    }


def test_parser_3():
    query = "SELECT a,b FROM tbl WHERE a = b and not b = 10 or a = 20"
    r = parse(query)
    assert r.__to_dict__() == {
        "targets": [
            "a",
            "b",
        ],
        "table": "tbl",
        "predicate": {
            "type": "AND",
            "p1": {
                "type": "ColumnToColumn",
                "op1": "a",
                "op2": "b",
            },
            "p2": {
                "type": "NOT",
                "p1": {
                    "type": "OR",
                    "p1": {
                        "type": "ColumnToValue",
                        "op1": "b",
                        "op2": 10,
                    },
                    "p2": {
                        "type": "ColumnToValue",
                        "op1": "a",
                        "op2": 20,
                    },
                },
                "p2": "None",
            },
        },
    }
