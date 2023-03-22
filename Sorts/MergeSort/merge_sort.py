
def merge(left_half, right_half):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            sorted_list.append(left_half[left_index])
            left_index += 1
        else:
            sorted_list.append(right_half[right_index])
            right_index += 1

    while left_index < len(left_half):
        sorted_list.append(left_half[left_index])
        left_index += 1

    while right_index < len(right_half):
        sorted_list.append(right_half[right_index])
        right_index += 1

    return sorted_list


def merge_sort(list_for_sort):
    if len(list_for_sort) <= 1:
        return list_for_sort

    mid_index = len(list_for_sort) // 2
    list_left_half = list_for_sort[:mid_index]
    list_right_half = list_for_sort[mid_index:]

    list_left_half = merge_sort(list_left_half)
    list_right_half = merge_sort(list_right_half)
    return merge(list_left_half, list_right_half)
