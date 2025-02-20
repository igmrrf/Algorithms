from collections import deque


class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)
        return [
            data,
            self.stack,
        ]

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return [data, self.stack]

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


stack = Stack()
print("Push:", stack.push(3))
print("Push:", stack.push(4))
print("Push:", stack.push(4))
print("Push:", stack.push(4))
print("Push:", stack.push(4))
print("Push:", stack.push(4))
print("Push:", stack.push(4))
print("Push:", stack.push(4))

print("Size:", stack.size())

print("Hello There")
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Size:", stack.size())
print("Empty:", stack.isEmpty())


class Stack2:

    def __init__(self):
        self.stack = deque()

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
