# pamietac zeby zrobic tez dal posortowanej listy

digits = [0, 2, 1, 6, 5, 8, 4, 7, 9, 3]


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self, root=None, height=0):
        self.root = root
        self.height = height

    def insert_node(self, node_value: int):
        if not self.root:
            self.root = Node(node_value)
            self.height = 1
        else:
            success = False
            node = self.root
            while not success:
                if node_value < node.value:
                    if not node.left_child:
                        node.left_child = Node(node_value)
                        self.height += 1
                        success = True
                    else:
                        node = node.left_child
                elif node_value > node.value:
                    if not node.right_child:
                        node.right_child = Node(node_value)
                        self.height += 1
                        success = True
                    else:
                        node = node.right_child

    def find_node():
        pass

    def delete_node(node_value):
        pass

    def print_tree():
        pass


tree = BinarySearchTree()

for i in range(len(digits)):
    tree.insert_node(digits[i])

print(tree.root)
