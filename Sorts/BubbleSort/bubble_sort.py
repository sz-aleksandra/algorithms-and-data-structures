from change_position import change_element_positions


def bubble_sort(list_for_sort):
    list_length = len(list_for_sort)
    for i in range(list_length):
        flag = False

        for j in range(0, list_length - i - 1):
            if list_for_sort[j] > list_for_sort[j + 1]:
                change_element_positions(list_for_sort, j, j+1)
                flag = True

        if not flag:
            break
