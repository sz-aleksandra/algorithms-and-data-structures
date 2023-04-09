from ..BST import Node, BinarySearchTree

# change_node_hegiht_after_deleting is not tested but its a part of delete_node test
# print_horizontally is not tested automaticly, but manually


def test_Node():
    node = Node(4)
    assert node.value == 4
    assert node.height == 1
    assert node.left_child is None
    assert node.right_child is None


def test_BinarySearchTree():
    digits = [0, 2, 1, 6]
    tree = BinarySearchTree()
    assert tree.root is None
    for i in range(len(digits)):
        tree.insert_rec(digits[i], tree.root)
    assert tree.root.value == 0
    assert tree.root.right_child.value == 2
    assert tree.root.right_child.left_child.value == 1
    assert tree.root.right_child.right_child.value == 6


def test_BST_delete_node():
    digits = [0, 2, 1, 6, 5, 8, 4, 7, 9, 3]
    tree = BinarySearchTree()
    for i in range(len(digits)):
        tree.insert_rec(digits[i], tree.root)
    tree.delete_node(9)
    assert tree.root.right_child.right_child.right_child.right_child is None
    tree.delete_node(8)
    assert tree.root.right_child.right_child.right_child.value == 7
    assert tree.root.right_child.right_child.right_child.right_child is None
    assert tree.root.right_child.right_child.right_child.left_child is None
    tree.delete_node(6)
    assert tree.root.right_child.right_child.value == 5
    assert tree.root.right_child.right_child.right_child.value == 7
    assert tree.root.right_child.right_child.left_child.value == 4
    assert tree.root.right_child.right_child.left_child.left_child.value == 3
    tree.delete_node(0)
    assert tree.root.value == 2
    assert tree.root.left_child.value == 1
    assert tree.root.right_child.value == 5
    assert tree.root.right_child.right_child.value == 7
    assert tree.root.right_child.left_child.value == 4
    assert tree.root.right_child.left_child.left_child.value == 3


def test_BTS_find_node():
    digits = [0, 2, 1, 6, 5, 8, 4, 7, 9, 3]
    tree = BinarySearchTree()
    for i in range(len(digits)):
        tree.insert_rec(digits[i], tree.root)
    assert tree.find_rec(None, tree.root, 10)[1] is None
    assert tree.find_rec(None, tree.root, 0)[0] is None
    assert tree.find_rec(None, tree.root, 0)[1].value == 0
    assert tree.find_rec(None, tree.root, 8)[0].value == 6
    assert tree.find_rec(None, tree.root, 8)[0].right_child.value == 8
    assert tree.find_rec(None, tree.root, 8)[1].value == 8
    assert tree.find_rec(None, tree.root, 8)[1].right_child.value == 9
    assert tree.find_rec(None, tree.root, 8)[1].left_child.value == 7


def test_BST_find_biggest_node_in_a_subtree():
    digits = [0, 2, 1, 6, 5, 8, 4, 7, 9, 3]
    tree = BinarySearchTree()
    for i in range(len(digits)):
        tree.insert_rec(digits[i], tree.root)
    assert tree.find_biggest_node_in_subtree(None, tree.root)[0].value == 8
    assert tree.find_biggest_node_in_subtree(None, tree.root)[1].value == 9
    assert tree.find_biggest_node_in_subtree(tree.root.right_child.right_child, tree.root.right_child.right_child.left_child)[0].value == 6
    assert tree.find_biggest_node_in_subtree(tree.root.right_child.right_child, tree.root.right_child.right_child.left_child)[1].value == 5
