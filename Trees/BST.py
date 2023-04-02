# pamietac zeby zrobic tez dal posortowanej listy

digits = [0, 2, 1, 6, 5, 8, 4, 7, 9, 3]


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f'{self.value}'


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert_node(self, node_value):
        if not self.root:
            self.root = Node(node_value)
        else:
            success = False
            node = self.root
            while not success:
                if node_value < node.value:
                    if not node.left_child:
                        node.left_child = Node(node_value)
                        success = True
                    else:
                        node = node.left_child
                elif node_value > node.value:
                    if not node.right_child:
                        node.right_child = Node(node_value)
                        success = True
                    else:
                        node = node.right_child

    def find_node(self, node_value):
        parent = None
        node = self.root
        while node:
            if node_value < node.value:
                parent = node
                node = node.left_child
            elif node_value > node.value:
                parent = node
                node = node.right_child
            else:
                return parent, node
        return parent, node

    def find_biggest_node_in_subtree(self, start_parent, start_node):
        parent = start_parent
        node = start_node
        while node.right_child:
            parent = node
            node = node.right_child
        return parent, node

    def delete_node(self, node_value):
        parent, node = self.find_node(node_value)
        if node:
            if node.left_child:
                if node.right_child:
                    # ma dwoje dzieci
                    new_parent, new_node = self.find_biggest_node_in_subtree(node, node.left_child)
                    new_node.right_child = node.right_child
                    if parent:
                        if parent.left_child.value == node.value:
                            parent.left_child = new_node
                        else:
                            parent.right_child = new_node
                    else:
                        self.root = new_node
                        self.root.right_child = node.right_child
                    new_parent.left_child = None
                else:
                    # ma lewe dziecko
                    if parent:
                        if parent.right_child:
                            if parent.right_child.value == node.value:
                                parent.right_child = node.left_child
                            else:
                                parent.left_child = node.left_child
                        else:
                            parent.left_child = node.left_child
                    else:
                        self.root = node.left_child
            else:
                if node.right_child:
                    # ma prawe dziecko
                    if parent:
                        if parent.left_child:
                            if parent.left_child.value == node.value:
                                parent.left_child = node.right_child
                            else:
                                parent.right_child = node.right_child
                        else:
                            parent.left_child = node.left_child
                    else:
                        self.root = node.right_child
                else:
                    # nie ma dzieci
                    if parent:
                        if parent.left_child.value == node.value:
                            parent.left_child = None
                        else:
                            parent.right_child = None
                    else:
                        self.root = None

    def print_tree():
        pass


tree = BinarySearchTree()

for i in range(len(digits)):
    tree.insert_node(digits[i])

print(tree.root)
print(tree.find_node(4))
print(tree.find_node(10))
tree.delete_node(7)
tree.delete_node(8)
tree.delete_node(4)
tree.delete_node(6)
tree.delete_node(0)
