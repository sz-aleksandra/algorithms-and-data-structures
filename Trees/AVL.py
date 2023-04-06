from BST import Node, BinarySearchTree

class AVLTree(BinarySearchTree):
    def insert_rec(self, node_value, node):
        super().insert_rec(node_value, node)
        self.rebalance(node)

    def delete_node(self, node_value):
        return super().delete_node(node_value)


    def rebalance(self, node):
        pass
