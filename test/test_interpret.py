from sqli.data.map.map_datasource import MapDataSource
from sqli.parser.parser import parse


def test_interpret_1():
    source = MapDataSource(
        {
            "students": [
                {
                    "id": 1,
                    "name": "name - 1",
                },
                {
                    "id": 2,
                    "name": "name - 2",
                },
            ],
        },
    )
    query = "SELECT id, name FROM students WHERE id=1"
    query = parse(query)
    view = query.execute(source)
    assert len(view) == 1
    assert next(view) == {
        "id": 1,
        "name": "name - 1",
    }
