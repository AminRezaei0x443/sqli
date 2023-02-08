import json


def jdict(d, pretty=True) -> str:
    return json.dumps(d, indent=4 if pretty else 0)
