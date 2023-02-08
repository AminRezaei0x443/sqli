from sqli.parser.parser import parse


def test_parser():
    query = "SELECT id, name FROM students WHERE id=1"
    r = parse(query)
    print(r)
