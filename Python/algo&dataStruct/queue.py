

class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)
        return [data, self.queue, ]

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return [data, self.queue]

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)


queue = Queue()

print("Enqueue:", queue.enqueue(3))
print("Enqueue:", queue.enqueue(4))
print("Enqueue:", queue.enqueue(5))
print("Enqueue:", queue.enqueue(6))
print("Enqueue:", queue.enqueue(7))
print("Enqueue:", queue.enqueue(8))
print("Enqueue:", queue.enqueue(9))
print("Enqueue:", queue.enqueue(10))
print("Size:", queue.size())
print("Hello There")
print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Size:", queue.size())
print("Empty:", queue.isEmpty())
