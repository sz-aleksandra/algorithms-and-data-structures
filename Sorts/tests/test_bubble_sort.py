from ..BubbleSort.bubble_sort import bubble_sort


def test_bubble_sort(sample_list):
    expected_list = sorted(sample_list)
    bubble_sort(sample_list)
    assert sample_list == expected_list