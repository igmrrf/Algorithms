def undogenerator():
    class UndoableGenerator:
        def __init__(self, gen):
            self.gen = gen
            self.history = []
            self._iterator = iter(gen)

        def prepend_item(self, item, gen):
            yield item  # Yield the item you want to add at the start
            yield from gen

        def next(self):
            try:
                value = next(self._iterator)
                self.history.append(value)
                return value
            except StopIteration:
                raise StopIteration("End of generator")

        def undo(self):
            if self.history:
                print(self.history)
                popped = self.history.pop()
                print(self.history)
                print(popped)
                self._iterator = self.prepend_item(popped, self._iterator)
                return self.history[-1] if self.history else None
            else:
                print("No previous state to undo.")
                return None

    def count_up_to(n):
        count = 1
        while count <= n:
            yield count
            count += 1

    # Example usage
    gen = UndoableGenerator(count_up_to(5))
    print(f"Undo 2: {gen.undo()}")
    print(f"1: {gen.next()}")  # Output: 1
    print(f"2: {gen.next()}")  # Output: 2

    # Undoing
    print(f"Undo 2: {gen.undo()}")
    print(f"Undo 2: {gen.undo()}")
    print(f"Undo 2: {gen.undo()}")

    # Trying to go forward again
    print(f"2: {gen.next()}")
    print(f"3: {gen.next()}")
    print(f"4: {gen.next()}")


undogenerator()


def generators():
    # TODO: Are generators objects or functions
    def count_up_to(n):
        count = 1
        while count <= n:
            yield count
            count += 1

    counter = count_up_to(5)

    while True:
        try:
            value = next(counter)
            print(f"Current value: {value}")

            # next_value = next(counter)
            # print(f"Next value is {next_value}, so current value is not the last")
            # counter = iter([value])
        except StopIteration:
            print("Reached the last value")
            break

            undogenerator(value)
