class Node (object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # 0(1)
    def size1(self):
        return self.size

    # 0(N) not so good
    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode

        return size

    def insertEnd1(self, data):
        self.size += 1
        actualNode = self.head

        while actualNode is not None:
            actualNode = actualNode.nextNode
            if actualNode is None:
                actualNode = Node(data)
                
        

    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def transverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode

    def remove(self, data):
        if self.head is None:
            return

        self.size = self.size - 1

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if (previousNode is None):
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode


class DoubleLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # 0(1)
    def size1(self):
        return self.size

    # 0(N) not so good
    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode

        return size

    def insertEnd1(self, data):
        self.size += 1
        actualNode = self.head

        while actualNode is not None:
            actualNode = actualNode.nextNode
            if actualNode is None:
                actualNode = Node(data)

    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def transverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode
     

    def remove(self, data):
        tempNode = head
        while tempNode != NULL:
            if tempNode == node:
                previousNode.nextNode = tempNode.nextNode
                tempNode = null
                return

            previousNode = tempNode
            tempNode = tempNode.nextNode


linkedlist = LinkedList()

linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)

linkedlist.transverseList()

linkedlist.remove(12)
linkedlist.remove(122)

linkedlist.insertStart(10)
linkedlist.insertEnd(21)

linkedlist.transverseList()

linkedlist.remove(31)
linkedlist.insertEnd(90)

linkedlist.transverseList()
