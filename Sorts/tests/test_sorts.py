from ..MergeSort.merge_sort import merge_sort
from ..BubbleSort.bubble_sort import bubble_sort


def test_merge_sort(sample_list):
    expected_list = sorted(sample_list)
    assert merge_sort(sample_list) == expected_list


def test_bubble_sort(sample_list):
    expected_list = sorted(sample_list)
    bubble_sort(sample_list)
    assert sample_list == expected_list
