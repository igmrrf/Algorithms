class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linkedlist is empty")
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "---->"
            itr = itr.next
        print(llstr)

    def push(self, data):
        node = Node(data, self.head)
        self.head = node
        self.print()

    def pull(self):
        first = self.head
        if first:
            self.head = first.next
        self.print()

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        item = self.head
        while item.next:
            item = item.next

        item.next = Node(data, None)
        self.print()

    def pop(self):
        item = self.head
        while item:
            if item.next and item.next.next is None:
                item.next = None
            else:
                item = item.next
        self.print()

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
        if index < 0 or index > self.get_length() - 1:
            raise Exception("invalid index")

        if index == 0:
            self.push(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr:
            if itr.next and itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next
        raise Exception(f"{data} not found")

    def insert_after_value(self, data, insert_data):
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == data:
                itr.next = Node(insert_data, itr.next)
                return
            itr = itr.next
        raise Exception(f"{data} not found")

    def remove_at(self, index):

        print(self.get_length())
        if index < 0 or index > self.get_length() - 1:
            raise Exception("invalid index")

        if index == 0 and self.head:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                if itr.next and itr.next.next:
                    itr.next = itr.next.next
                else:
                    itr.next = None
                break
            itr = itr.next
            count += 1


ll = LinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print()
ll.insert_after_value("mango", "apple")
ll.print()
ll.remove_by_value("orange")  # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()
