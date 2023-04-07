from BST import BinarySearchTree


class AVLTree(BinarySearchTree):
    def insert_rec(self, node_value, node):
        super().insert_rec(node_value, node)
        self.insert_rebalance(node)

    def insert_rebalanace(self, node):
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left_child) >= 0:
            return self._rotate_left

    def _get_balance(self, node):
        if not node:
            return 0

        return self._get_height(node.left_child) - self._get_height(node.right_child)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _rotate_left(self, node):
        right_node = node.right_child
        right_node_left_child = right_node.left_child

        right_node.left_child = node
        node.right_child = right_node_left_child

        return right_node

    def _rotate_right(self, node):
        left_node = node.left_child
        left_node_right_child = left_node.right_child

        left_node.right_child = node
        node.left_child = left_node_right_child

        return left_node
