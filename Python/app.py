listUnlisited = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# class Node(object):
#     def __init__(self, data = None, nextNode = None):
#         self.data = data;
#         self.nextNode = nextNode;

# class LinkedList(object):
#     def __init__(self):
#         self.head = None;
#         self.size = 0;

#     def insertStart(self,data):

#         self.size = self.size + 1;
#         newNode = Node(data);

#         if not self.head:
#             self.head = newNode;

#         else:
#             newNode.nextNode = self.head;
#             self.head = newNode;

#     def size1(self):
#         return self.size

#     def insertEnd(self,data):
#         self.size = self.size + 1;
#         newNode = Node(data);
#         actualNode = self.head;

#         while actualNode.nextNode is not None:
#             actualNode = actualNode.nextNode

#         actualNode.nextNode = newNode;

#     def remove(self,data):
#         if self.head is None:
#             return;
#         self.size -= 1;

#         currentNode = self.head;
#         previousNode = None;

#         while currentNode.data != data:
#             previousNode = currentNode;
#             currentNode = currentNode.nextNode

#         if previousNode is None:
#             self.head = currentNode.nextNode;
#         else:
#             previousNode.nextNode = currentNode.nextNode


#     def size2(self):
#         actualNode = self.head;
#         size = 0;

#         while actualNode is not None:
#             size += 1;
#             actualNode = actualNode.nextNode;

#         return size

#     def traverselist(self):
#         actualNode = self.head;

#         while actualNode is not None:
#             print("%d " % actualNode.data);
#             actualNode = actualNode.nextNode;

#     def removedouble(Node, node):
#         node.previousNode.nextNode = node.nextNode;
#         node.nextNode.previousNode = node.previousNode;


# linkedlist = LinkedList();

# linkedlist.insertStart(12);
# linkedlist.insertStart(122)
# linkedlist.insertStart(50)
# linkedlist.insertStart(3)
# linkedlist.insertEnd(32)

# linkedlist.traverselist()
# print("Deleting")
# linkedlist.remove(32)
# linkedlist.remove(12)
# linkedlist.remove(122)
# linkedlist.remove(50)
# linkedlist.remove(3)

# print(linkedlist.size1())


#Showing the decimal that exist more than once
# def findDuplicate(nums):
#     tortoise = nums[0]
#     hare = nums[0]
#     while True:
#         tortoise = nums[tortoise]
#         hare = nums[nums[hare]]
#         if tortoise == hare:
#             break

#     ptr1 = nums[0]
#     ptr2 = tortoise
#     while ptr1 != ptr2:
#         ptr1 = nums[ptr1]
#         ptr2 = nums[ptr2]

#     return ptr1


# print(findDuplicate([3,4,3,2,5,7]))

def factorial(data):

    if (data == 0):
        return 1
    return data * factorial(data-1)


print(factorial(4))
