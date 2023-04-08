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
        elif node_value < node.value:
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

    def _get_node_with_min_value(self, node):
        if not node or not node.left_child:
            return node
        return self._get_node_with_min_value(node.left_child)

    def delete_node(self, node_value):
        self.root = self._delete_node(self.root, node_value)

    def _delete_node(self, node, node_value):
        if not node:
            return node
        elif node_value < node.value:
            node.left_child = self._delete_node(node.left_child, node_value)
        elif node_value > node.value:
            node.right_child = self._delete_node(node.right_child, node_value)
        else:
            # in this case node has one child or none
            if not node.left_child:
                temp_node = node.right_child
                node = None
                return temp_node
            elif not node.right_child:
                temp_node = node.left_child
                node = None
                return temp_node
            # in this case node has both children
            temp_node = self._get_node_with_min_value(node.right_child)
            node.value = temp_node.value
            node.right_child = self._delete_node(node.right_child, temp_node.value)
        return node

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
