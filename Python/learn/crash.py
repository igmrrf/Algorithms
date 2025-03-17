# Meta classes define how classes behave (like interfaces)
from abc import ABC, abstractmethod


class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"creating class: {name}")
        print(f"creating class: {bases}")
        print(f"creating class: {dct}")

        dct["custom_attr"] = 42
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=Meta):
    pass


class Person:
    def __init__(self, age) -> None:
        self.name = "francis"
        self.age = age
        pass

    def get_name(self):
        return self.name

    def get_info(self):
        return {"age": self.age, "name": self.name}


person = Person(23)
print(person.get_name())
print(person.get_info())


print(MyClass.custom_attr)
