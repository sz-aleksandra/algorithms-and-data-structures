class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert_ite(self, node_value):
        parent = None
        node = self.root
        new = Node(node_value)
        while node is not None:
            if new.value < node.value:
                parent = node
                node = node.left_child
            else:
                # new.value >= node.value
                parent = node
                node = node.right_child
        if parent is None:
            # there is no root
            self.root = new
        elif new.value < parent.value:
            parent.left_child = new
        elif new.value > parent.value:
            parent.right_child = new

    def find_rec(self, parent, node, node_value, depth=0, max_depth=None):
        if max_depth is not None and depth >= max_depth:
            return None

        if node:
            if node_value < node.value:
                return self.find_rec(node, node.left_child, node_value, depth=depth+1, max_depth=max_depth)
            elif node_value > node.value:
                return self.find_rec(node, node.right_child, node_value, depth=depth+1, max_depth=max_depth)
        return parent, node

    def find_ite(self, node_value):
        parent = None
        node = self.root
        while node:
            if node_value < node.value:
                parent = node
                node = node.left_child
            elif node_value > node.value:
                parent = node
                node = node.right_child
            elif node_value == node.value:
                return parent, node
        return None, None

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

        node.height = 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))
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
