import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


# Frozen true makes the class read-only
# The data is now immutable
@dataclass(frozen=False)
class Person:
    # def __init__(self, name: str, address: str):
    # 	self.name = name
    # 	self.address = address

    # def __str__(self) -> str:
    # 	return f"{self.name} lives at {self.address}"
    name: str
    address: str
    active: bool = True  # default value of True
    email_addresses: list[str] = field(default_factory=list)  # list is a function
    # init=False, means variable will not be part of __init__
    # Thus user won't be able to set value in param
    # Here we block custom id value
    id: str = field(init=False, default_factory=generate_id)
    # search_string is a protected method, and we don't want it included in __repr__
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"


if __name__ == "__main__":
    person = Person(name="John", address="123 Main St")
    print(person)
