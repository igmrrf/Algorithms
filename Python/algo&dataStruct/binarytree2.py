class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def sum(self):
        elements = 0
        elements += self.data

        if self.left:
            elements += self.left.sum()

        if self.right:
            elements += self.right.sum()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def add_child(self, node):
        if node.data > self.data:
            if self.right:
                self.right.add_child(node)
            else:
                self.right = node
                self.right.parent = self
        elif node.data < self.data:
            if self.left:
                self.left.add_child(node)
            else:
                self.left = node
                self.left.parent = self
        elif node.data == self.data:
            print("equal value")

    def get_node(self, data):
        if data > self.data:
            if self.right:
                return self.right.get_node(data)
        elif data < self.data:
            if self.left:
                return self.left.get_node(data)
        else:
            return self

    def remove_node(self, data):
        # Search for the node to remove
        if data < self.data:
            if self.left:
                self.left = self.left.remove_node(data)  # Update left child reference
        elif data > self.data:
            if self.right:
                self.right = self.right.remove_node(
                    data
                )  # Update right child reference
        else:
            # Case 1: Node has no children (Leaf Node)
            if not self.left and not self.right:
                if self.parent is None:
                    return None
                return None  # Remove the leaf node by returning None

            # Case 2: Node has only one child (Right child exists)
            if not self.left:
                if self.parent is None:
                    return self.right
                return self.right  # Replace node with right child

            # Case 2: Node has only one child (Left child exists)
            if not self.right:
                if self.parent is None:
                    return self.left
                return self.left  # Replace node with left child

            # Case 3: Node has two children
            min_larger_value = self.right.find_min()
            self.data = min_larger_value
            self.right = self.right.remove_node(min_larger_value)

            # # Replace with max small value
            # max_small_value = self.left.find_max()
            # self.data = max_small_value
            # self.right = self.right.remove_node(max_small_value)

        return self  # Return updated node reference to maintain tree structure

    def search(self, data):
        if data == self.data:
            return True
        elif data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False
        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        return False

    def get_level(self) -> int:
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_tree(self, dept=0):
        level = self.get_level()

        if dept and level > dept:
            return
        extra = ""
        if level:
            for i in range(level):
                extra += "    "
        extra = extra + "|__" if self.parent else ""

        print(extra, self.data)
        if self.left:
            self.left.print_tree(dept)
        if self.right:
            self.right.print_tree(dept)


def build_product_tree(elements):
    root = BinaryNode(15)

    for i in range(1, len(elements)):
        print(i)
        root.add_child(BinaryNode(elements[i]))

    return root


if __name__ == "__main__":
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    # elements = []

    root = build_product_tree(elements)
    print(root)

    root.remove_node(15)
    print(root)

    root = root.remove_node(15)
    print(root)
    if root:
        root.print_tree(4)
    pass
