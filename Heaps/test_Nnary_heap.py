from Nnary_heap import Nnary_Heap
import pytest


@pytest.fixture
def binary_heap_fixture():
    heap = Nnary_Heap(2)
    digits = [5, 3, 7, 1, 4, 6, 2]
    for digit in digits:
        heap.push(digit)
    return heap


@pytest.fixture
def ternary_heap_fixture():
    heap = Nnary_Heap(3)
    digits = [5, 3, 7, 1, 4, 6, 2]
    for digit in digits:
        heap.push(digit)
    return heap


@pytest.fixture
def quaternary_heap_fixture():
    heap = Nnary_Heap(4)
    digits = [5, 3, 7, 1, 4, 6, 2]
    for digit in digits:
        heap.push(digit)
    return heap


def test_binary_heap_creation(binary_heap_fixture):
    assert binary_heap_fixture.heap_as_list[0] == 7
    assert binary_heap_fixture.heap_as_list[1] == 4
    assert binary_heap_fixture.heap_as_list[2] == 6
    assert binary_heap_fixture.heap_as_list[3] == 1
    assert binary_heap_fixture.heap_as_list[4] == 3
    assert binary_heap_fixture.heap_as_list[5] == 5
    assert binary_heap_fixture.heap_as_list[6] == 2


def test_binary_heap_pop_root(binary_heap_fixture):
    assert binary_heap_fixture.heap_as_list[0] == 7
    binary_heap_fixture.pop_root()
    assert binary_heap_fixture.heap_as_list[0] == 6


def test_ternary_heap_creation(ternary_heap_fixture):
    assert ternary_heap_fixture.heap_as_list[0] == 7
    assert ternary_heap_fixture.heap_as_list[1] == 6
    assert ternary_heap_fixture.heap_as_list[2] == 5
    assert ternary_heap_fixture.heap_as_list[3] == 1
    assert ternary_heap_fixture.heap_as_list[4] == 3
    assert ternary_heap_fixture.heap_as_list[5] == 4
    assert ternary_heap_fixture.heap_as_list[6] == 2


def test_ternary_heap_pop_root(ternary_heap_fixture):
    assert ternary_heap_fixture.heap_as_list[0] == 7
    ternary_heap_fixture.pop_root()
    assert ternary_heap_fixture.heap_as_list[0] == 6
    assert ternary_heap_fixture.heap_as_list[1] == 4


def test_quaternary_heap_pop_creation(quaternary_heap_fixture):
    assert quaternary_heap_fixture.heap_as_list[0] == 7
    assert quaternary_heap_fixture.heap_as_list[1] == 6
    assert quaternary_heap_fixture.heap_as_list[2] == 5
    assert quaternary_heap_fixture.heap_as_list[3] == 1
    assert quaternary_heap_fixture.heap_as_list[4] == 4
    assert quaternary_heap_fixture.heap_as_list[5] == 3
    assert quaternary_heap_fixture.heap_as_list[6] == 2


def test_quaternary_heap_pop_root(quaternary_heap_fixture):
    assert quaternary_heap_fixture.heap_as_list[0] == 7
    quaternary_heap_fixture.pop_root()
    assert quaternary_heap_fixture.heap_as_list[0] == 6
    assert quaternary_heap_fixture.heap_as_list[1] == 3
    assert quaternary_heap_fixture.heap_as_list[5] == 2