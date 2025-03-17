# Descriptors (custom getters and setters)
class Descriptor:
    def __get__(self, instance, owner):
        return instance.value

    def __set__(self, instance, value):
        instance.value = value * 2


class Test:
    attr = Descriptor()


# Abstract Base Classes
class AbstractClass(ABC):
    @abstractmethod
    def do_something(self):
        pass


class ConcreteClass(AbstractClass):
    def do_something(self):
        return "Implemented!"


# Decorators: These are a powerful way of adding/modifying the behaving of methods and functions by wrappting them.
# Decorators using contain repetitive functionalities that are used in multiple instances, examples use are for authentication,
# caching, routing, etc
# TODO: check how to access the parameters of a function passed to a decorator
def decorator(func):
    print("even before the wrapper")

    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")

    return wrapper


# Generators: These are functions that allow you to iterate over a possible infinity sequence of data without having to store the entire sequence in memory


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
