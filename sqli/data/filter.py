class Filter:
    value: dict[int, bool]

    def __init__(self, value: dict[int, bool] = None) -> None:
        self.value = value or {}

    def add(self, id_: int, state: bool):
        self.value[id_] = state

    def add_positive(self, id_: int):
        self.value[id_] = True

    def add_negative(self, id_: int):
        self.value[id_] = False

    def __getitem__(self, id_: int) -> bool:
        return self.value[id_]

    def __and__(self, other: "Filter") -> "Filter":
        if not isinstance(other, Filter):
            raise RuntimeError("Unsupported and operand for Filter!")
        new_value = {k: v and other[k] for k, v in self.value.items()}
        return Filter(new_value)

    def __or__(self, other: "Filter") -> "Filter":
        if not isinstance(other, Filter):
            raise RuntimeError("Unsupported and operand for Filter!")
        new_value = {k: v or other[k] for k, v in self.value.items()}
        return Filter(new_value)

    def __invert__(self) -> "Filter":
        new_value = {k: not v for k, v in self.value.items()}
        return Filter(new_value)
