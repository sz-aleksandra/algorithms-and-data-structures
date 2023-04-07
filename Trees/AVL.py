from BST import BinarySearchTree


class AVLTree(BinarySearchTree):
    def insert_rec(self, node_value, node):
        super().insert_rec(node_value, node)
        if self._get_balance(node) < -1:
            if node.right_child and self._get_balance(node.right_child) < 0:
                self._rotate_left(node)
            else:
                self._rotate_right(node)
                self._rotate_left(node)
        elif self._get_balance(node) > 1:
            if node.left_child and self._get_balance(node.left_child) > 0:
                self._rotate_right(node)
            else:
                self._rotate_left(node)
                self._rotate_right(node)

    def delete_node(self, node_value):
        self.root = self._delete_node(self.root, node_value)

    def _delete_node(self, node, node_value)
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


    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left_child) - self._get_height(node.right_child)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_node_with_min_value(self, node):
        if not node or not node.left_child:
            return node
        return self._get_node_with_min_value(node.left_child)

    def _rotate_left(self, node):
        if not node or not node.right_child:
            return
        right_node = node.right_child
        right_node_left_child = right_node.left_child
        right_node.left_child = node
        node.right_child = right_node_left_child

        node.height = 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))
        right_node.height = 1 + max(self._get_height(right_node.left_child), self._get_height(right_node.right_child))

        return right_node

    def _rotate_right(self, node):
        if not node or not node.left_child:
            return
        left_node = node.left_child
        left_node_right_child = left_node.right_child
        left_node.right_child = node
        node.left_child = left_node_right_child

        node.height = 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))
        left_node.height = 1 + max(self._get_height(left_node.left_child), self._get_height(left_node.right_child))

        return left_node




