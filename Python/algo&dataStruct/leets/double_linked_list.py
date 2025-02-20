class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_backward(self):
        if self.head is None:
            print("Linkedlist is empty")

        itr = self.head
        llstr = ""
        while itr:
            llstr = str(itr.data) + "---->" + llstr
            itr = itr.next
        print(llstr)

    def print_forward(self):
        if self.head is None:
            print("Linkedlist is empty")
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "---->"
            itr = itr.next
        print(llstr)

    def push(self, data):
        node = Node(data, self.head, None)
        if self.head:
            self.head.prev = node

        self.head = node

    def pull(self):
        if self.head is None:
            raise Exception("linkedlist is empty")

        itr = self.head
        if itr:
            if itr.next:
                self.head = itr.next
                self.head.prev = None
            else:
                self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        item = self.head
        while item.next:
            item = item.next

        item.next = Node(data, None, item)

    def pop(self):
        if self.head is None:
            raise Exception("linkedlist is empty")

        item = self.head
        while item.next:
            item = item.next

        if item.prev:
            item.prev.next = None

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.append(data)

    def get_length(self):
        count = 0
        item = self.head

        while item:
            count += 1
            item = item.next

        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.push(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                node = Node(data, itr, itr.prev)
                if itr.prev:
                    itr.prev.next = node
                itr.prev = node
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr:
            if itr.data == data:
                if itr.prev:
                    itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                return
            itr = itr.next
        raise Exception(f"{data} not found")

    def insert_after_value(self, data, insert_data):
        if self.head is None:
            raise Exception("linkedlist is empty")

        itr = self.head
        while itr:
            if itr.data == data:
                node = Node(insert_data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                return
            itr = itr.next
        raise Exception(f"{data} not found")

    def remove_at(self, index):
        if index < 0 or index > self.get_length() - 1:
            raise Exception("invalid index")

        if index == 0 and self.head:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                if itr.next:
                    itr.next.prev = itr.prev
                if itr.prev:
                    itr.prev.next = itr.next
                break
            itr = itr.next
            count += 1


ll = DoubleLinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print_forward()
ll.print_backward()
ll.append("figs")
ll.print_forward()
ll.insert_at(0, "jackfruit")
ll.print_forward()
ll.insert_at(6, "dates")
ll.print_forward()
ll.insert_at(2, "kiwi")
ll.print_forward()
