# pamietac zeby zrobic tez dal posortowanej listy

digits = [0, 2, 1, 6, 5, 8, 4, 7, 9, 3]


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 1

    def __str__(self):
        return f'{self.value}'

#    def __eq__(self, other_node):
#        return self.value == other_node.value and self.left_child == other_node.left_child and self.right_child == other_node.right_child


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

            if node.left_child and node.right_child:
                node.height = 1 + max(node.left_child.height, node.right_child.height)
            elif node.left_child:
                node.height = 1 + node.left_child.height
            elif node.right_child:
                node.height = 1 + node.right_child.height
            else:
                node.height = 1




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
        parent, node = self.find_node(node_value)
        if node:
            if node.left_child:
                if node.right_child:
                    # ma dwoje dzieci
                    new_parent, new_node = self.find_biggest_node_in_subtree(node, node.left_child)  # szukamy najwiekszego wezla w poddrzewie mniejszych zeby zastapic usuwany wezel
                    new_node.right_child = node.right_child  # podlaczamy prawe dzieci usuwanego wezla do nowego
                    if new_node != node.left_child:  #jesli dziecko usuwanego wezla nie mialoby zadnych prawych dzieci (jest najwiekszym elementem lewego poddrzewa) to nie trzeba podlaczac dzieci usuwanego wezla do niego
                        new_node.left_child = node.left_child
                    if parent:
                        if parent.left_child == node:
                            parent.left_child = new_node
                        else:
                            parent.right_child = new_node
                    else:
                        self.root = new_node
                    new_parent.left_child = None  # odlaczamy wezel ktorym zastepujemy usuniety wezel od jego rodzica
                else:
                    # ma lewe dziecko
                    if parent:
                        if parent.right_child == node:
                            parent.right_child = node.left_child
                        else:
                            parent.left_child = node.left_child
                    else:
                        self.root = node.left_child
            else:
                if node.right_child:
                    # ma prawe dziecko
                    if parent:
                        if parent.left_child == node:
                            parent.left_child = node.right_child
                        else:
                            parent.right_child = node.right_child
                    else:
                        self.root = node.right_child
                else:
                    # nie ma dzieci
                    if parent:
                        if parent.left_child == node:
                            parent.left_child = None
                        else:
                            parent.right_child = None
                    else:
                        self.root = None

    def find_height(self, node):
        if not node:
            return 0
        else:
            left_height = self.find_height(node.left_child)
            right_height = self.find_height(node.right_child)
            return max(left_height, right_height) + 1

    def print_horizontally(self, left, level, node):
        if node:
            self.print_horizontally(0, level + 1, node.right_child)
            if node == self.root:
                print(F"{'  ' * level}*{node}*")
            elif left:
                print(F"{'  ' * level}\*{node}*")
            else:
                print(F"{'  ' * level}/*{node}*")
            self.print_horizontally(1, level + 1, node.left_child)


tree = BinarySearchTree()

for i in range(len(digits)):
    tree.insert_rec(digits[i], tree.root)


#print(tree.root)
#print(tree.find_rec(None, tree.root, 4))
#print(tree.find_rec(None, tree.root, 10))
tree.print_horizontally(0, 0, tree.root)
#print(tree.find_biggest_node_in_subtree(tree.root.right_child, tree.root.right_child.left_child))
#tree.delete_node(2)
#tree.delete_node(7)
#tree.delete_node(8)
#tree.delete_node(4)
#tree.delete_node(6)
#tree.delete_node(0)
