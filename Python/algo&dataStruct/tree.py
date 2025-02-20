class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self) -> int:
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_tree(self, type, dept=0):
        level = self.get_level()

        if dept and level > dept:
            return
        extra = ""
        if level:
            for i in range(level):
                extra += "    "
        extra = extra + "|__" if self.parent else ""

        if type == "name":
            print(extra, self.name)
        elif type == "designation":
            print(extra, self.designation)
        else:
            print(f"{extra} {self.name} ({self.designation})")
        for child in self.children:
            child.print_tree(type, dept)


def build_product_tree():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinway", "CTO")

    infra = TreeNode("Vishwa", "Infrastructure Head")
    infra.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra.add_child(TreeNode("Abhijit", "App Manager"))

    hr = TreeNode("Gels", "HR Head")
    hr.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr.add_child(TreeNode("Waqas", "Policy Mangager"))

    cto.add_child(infra)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    root.add_child(cto)
    root.add_child(hr)

    return root

    # laptop = TreeNode('Laptop')


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree("full", 1)
    pass
