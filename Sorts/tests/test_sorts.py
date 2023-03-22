from ..MergeSort.merge_sort import merge_sort
from ..BubbleSort.bubble_sort import bubble_sort
from ..SelectionSort.selection_sort import selection_sort
import pytest


@pytest.fixture
def sample_list():
    return ['a', 'b', 'c', 'd', 'E', 'A', 'Abecadło',
            '123', '1', '0', 'Litwo', 'Pan', 'Tadeusz', 'Mickiewicz']


def test_merge_sort(sample_list):
    expected_list = sorted(sample_list)
    assert merge_sort(sample_list) == expected_list


def test_bubble_sort(sample_list):
    expected_list = sorted(sample_list)
    bubble_sort(sample_list)
    assert sample_list == expected_list


def test_selection_sort(sample_list):
    expected_list = sorted(sample_list)
    selection_sort(sample_list)
    assert sample_list == expected_list
