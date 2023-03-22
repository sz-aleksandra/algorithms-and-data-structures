from MergeSort.merge_sort import merge_sort


def test_merge_sort(sample_list):
    expected_list = sorted(sample_list)
    assert merge_sort(sample_list) == expected_list
