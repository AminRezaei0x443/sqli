from sqli import MapDataSource, parse


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


def test_interpret_2():
    # This toy dataset we use is a random sample from:
    # https://www.kaggle.com/datasets/carlolepelaars/toy-dataset
    source = MapDataSource.from_csv({"people": "test/data/toy_csv.csv"})
    query = "SELECT Number, City FROM people WHERE Age=50"
    query = parse(query)
    view = query.execute(source)
    assert len(view) == 14


def test_interpret_3():
    # This toy dataset we use is a random sample from:
    # https://www.kaggle.com/datasets/carlolepelaars/toy-dataset
    source = MapDataSource.from_csv({"people": "test/data/toy_csv.csv"})
    query = 'SELECT Number, City FROM people WHERE Age=50 and Gender="Female" or not Illness="No" and not Gender=Illness'
    query = parse(query)
    view = query.execute(source)
    assert len(view) == 7
