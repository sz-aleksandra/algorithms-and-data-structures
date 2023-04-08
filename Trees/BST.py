class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert_rec(self, node_value, node):
        if not node:
            self.root = Node(node_value)
        else:
            if node_value < node.value:
                if node.left_child:
                    self.insert_rec(node_value, node.left_child)
                else:
                    node.left_child = Node(node_value)
            elif node_value > node.value:
                if node.right_child:
                    self.insert_rec(node_value, node.right_child)
                else:
                    node.right_child = Node(node_value)

    def find_rec(self, parent, node, node_value):
        if node:
            if node_value < node.value:
                return self.find_rec(node, node.left_child, node_value)
            elif node_value > node.value:
                return self.find_rec(node, node.right_child, node_value)
        return parent, node

    def find_biggest_node_in_subtree(self, parent, node):
        while node.right_child:
            parent = node
            node = node.right_child
        return parent, node

    def delete_node(self, node_value):
        parent, node = self.find_rec(None, self.root, node_value)
        if node:
            if node.left_child:
                if node.right_child:
                    # has two children
                    new_parent, new_node = self.find_biggest_node_in_subtree(node, node.left_child)
                    new_node.right_child = node.right_child
                    if new_node != node.left_child:
                        new_node.left_child = node.left_child
                    if parent:
                        if parent.left_child == node:
                            parent.left_child = new_node
                        else:
                            parent.right_child = new_node
                    else:
                        self.root = new_node
                    new_parent.left_child = None
                else:
                    # has left child
                    if parent:
                        if parent.right_child == node:
                            parent.right_child = node.left_child
                        else:
                            parent.left_child = node.left_child
                    else:
                        self.root = node.left_child
            else:
                if node.right_child:
                    # has right child
                    if parent:
                        if parent.left_child == node:
                            parent.left_child = node.right_child
                        else:
                            parent.right_child = node.right_child
                    else:
                        self.root = node.right_child
                else:
                    # does not have children
                    if parent:
                        if parent.left_child == node:
                            parent.left_child = None
                        else:
                            parent.right_child = None
                    else:
                        self.root = None

    def print_horizontally(self, left, level, node):
        if node:
            self.print_horizontally(0, level + 1, node.right_child)
            if node == self.root:
                print(f"{'  ' * level}*{node.value}*")
            elif left:
                print(f"{'  ' * level}\\*{node.value}*")
            else:
                print(f"{'  ' * level}/*{node.value}*")
            self.print_horizontally(1, level + 1, node.left_child)
