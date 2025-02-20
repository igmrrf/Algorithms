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

    def min(self):
        if self.left:
            return self.left.min()
        return self.data

    def max(self):
        if self.right:
            return self.right.max()
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
                return None  # Remove the leaf node by returning None

            # Case 2: Node has only one child (Right child exists)
            if not self.left:
                return self.right  # Replace node with right child

            # Case 2: Node has only one child (Left child exists)
            if not self.right:
                return self.left  # Replace node with left child

            # Case 3: Node has two children
            min_larger_node = self.right  # Find the minimum node in the right subtree
            while min_larger_node.left:
                min_larger_node = min_larger_node.left

            self.data = min_larger_node.data  # Copy value to current node
            self.right = self.right.remove_node(
                min_larger_node.data
            )  # Remove the duplicate

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


def build_product_tree():
    root = BinaryNode(15)
    root.add_child(BinaryNode(27))
    root.add_child(BinaryNode(12))
    root.add_child(BinaryNode(14))
    root.add_child(BinaryNode(7))
    root.add_child(BinaryNode(20))
    root.add_child(BinaryNode(88))
    root.add_child(BinaryNode(23))
    root.add_child(BinaryNode(13))
    root.add_child(BinaryNode(5))
    root.add_child(BinaryNode(6))
    root.add_child(BinaryNode(4))

    return root

    # laptop = TreeNode('Laptop')


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree(4)
    root.remove_node(12)
    root.print_tree(4)
    print(root.in_order_traversal())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())
    print("Max: ", root.max())
    print("Min: ", root.min())
    print("Sum: ", root.sum())

    pass
