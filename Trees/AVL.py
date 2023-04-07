from BST import Node, BinarySearchTree


class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 1


class AVLTree(BinarySearchTree):
    def insert_rec(self, node_value, node):
        super().insert_rec(node_value, node)
        self.rebalance(node)

    def rebalanace(self, node):
        pass



    def _get_balance(self, node):
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
