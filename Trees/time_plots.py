from random import randint
from AVL import AVLTree
from BST import BinarySearchTree
import time
import gc
from matplotlib import pyplot as plt
import sys


def random_list_generator():
    return [randint(1, 30000) for _ in range(10000)]


n_range = range(1000, 11000, 1000)


def measure_bst_operations_time():
    bst_creation_times = {}
    bst_finding_times = {}
    bst_deleting_times = {}
    for n in n_range:
        sys.setrecursionlimit(n)

        gc_old = gc.isenabled()
        gc.disable()
        input_list = random_list_generator()[:n]
        bst_tree = BinarySearchTree()
        start_creation_time = time.process_time()
        for digit in input_list:
            bst_tree.insert_rec(digit, bst_tree.root)
        finish_creation_time = time.process_time()
        bst_creation_times[n] = finish_creation_time - start_creation_time

        start_finding_time = time.process_time()
        for digit in input_list:
            bst_tree.find_rec(None, bst_tree.root, digit)
        finish_finding_time = time.process_time()
        bst_finding_times[n] = finish_finding_time - start_finding_time

        start_deletion_time = time.process_time()
        for digit in input_list:
            bst_tree.delete_node(digit)
        finish_deletion_time = time.process_time()
        bst_deleting_times[n] = finish_deletion_time - start_deletion_time
        if gc_old:
            gc.enable()
    return {
        "creation": bst_creation_times,
        "finding": bst_finding_times,
        "deletion":  bst_deleting_times
        }


def measure_avl_operations_time():
    avl_creation_times = {}
    avl_finding_times = {}
    avl_deletion_times = {}
    for n in n_range:
        sys.setrecursionlimit(n)

        gc_old = gc.isenabled()
        gc.disable()
        input_list = random_list_generator()[:n]
        avl_tree = AVLTree()
        start_creation_time = time.process_time()
        for digit in input_list:
            avl_tree.insert_node(digit)
        finish_creation_time = time.process_time()
        avl_creation_times[n] = finish_creation_time - start_creation_time

        start_finding_time = time.process_time()
        for digit in input_list:
            avl_tree.find_rec(None, avl_tree.root, digit)
        finish_finding_time = time.process_time()
        avl_finding_times[n] = finish_finding_time - start_finding_time

        start_deletion_time = time.process_time()
        for digit in input_list:
            avl_tree.delete_node(digit)
        finish_deletion_time = time.process_time()
        avl_deletion_times[n] = finish_deletion_time - start_deletion_time
        if gc_old:
            gc.enable()
    return {
        "creation": avl_creation_times,
        "finding": avl_finding_times,
        "deletion": avl_deletion_times
        }


def plot_creation(title, operation):
    plt.plot(
        measure_bst_operations_time()[operation].keys(),
        measure_bst_operations_time()[operation].values(),
        '-',
        label=f'bst {operation} plots',
        markersize=3
        )
    plt.plot(
        measure_avl_operations_time()[operation].keys(),
        measure_avl_operations_time()[operation].values(),
        '-',
        label=f'avl {operation} plots',
        markersize=3
        )
    plt.legend()
    plt.xlabel('Amount of digits')
    plt.ylabel('Time in seconds')
    plt.title(label=f'Time of {operation}')
    figure = plt.gcf()
    figure.savefig(title, format='png')


plot_creation('creation_time.png', 'creation')
plot_creation('finding_time.png', 'finding')
plot_creation('deletion_time.png', 'deletion')
