from AVL import AVLTree
import pytest


@pytest.fixture
def sample_avl_tree():
    avl_tree = AVLTree()
    digits = [1, 2, 8, 4]
    for digit in digits:
        avl_tree.insert_node(digit)
    return avl_tree

def test_insertion_of_node(sample_avl_tree):
    assert sample_avl_tree.root.value == 2
    assert sample_avl_tree.root.left_child.value == 1
    assert sample_avl_tree.root.right_child.value == 8
    assert sample_avl_tree.root.right_child.left_child.value == 4


def test_deletion_of_node(sample_avl_tree):
    assert sample_avl_tree.root.right_child.value == 8
    sample_avl_tree.delete_node(8)
    assert sample_avl_tree.root.right_child.value == 4
    assert sample_avl_tree.find_ite(8) == (None, None)


def test_get_balance(sample_avl_tree):
    assert sample_avl_tree._get_balance(sample_avl_tree.root) == -1
    assert sample_avl_tree._get_balance(sample_avl_tree.root.right_child) == 1


def test_get_height(sample_avl_tree):
    assert sample_avl_tree._get_height(sample_avl_tree.root) == 3
    assert sample_avl_tree._get_height(sample_avl_tree.root.left_child) == 1


def test_get_node_with_min_value(sample_avl_tree):
    assert sample_avl_tree._get_node_with_min_value(sample_avl_tree.root).value == 1


def test_rotate_left(sample_avl_tree):
    assert sample_avl_tree._rotate_left(sample_avl_tree.root).value == 8
    assert sample_avl_tree.root.value == 2
    assert sample_avl_tree.root.left_child.value == 1
    assert sample_avl_tree.root.right_child.value == 4


def test_rotate_right(sample_avl_tree):
    assert sample_avl_tree._rotate_right(sample_avl_tree.root).value == 1
    assert sample_avl_tree.root.value == 2
    assert not sample_avl_tree.root.left_child
    assert sample_avl_tree.root.right_child.value == 8
    assert sample_avl_tree.root.right_child.left_child.value == 4
