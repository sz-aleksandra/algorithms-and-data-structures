from random import randint
from change_position import change_element_positions


def quick_sort(words, start, end):
    # quick sort with Lomuto partition scheme
    if start < end:
        pick = randint(start, end)
        pick_value = words[pick]
        change_element_positions(words, end, pick)
        current_position = start
        for i in range(start, end):
            if words[i] < pick_value:
                change_element_positions(words, i, current_position)
                current_position = current_position + 1
        change_element_positions(words, current_position, end)
        quick_sort(words, start, current_position - 1)
        quick_sort(words, current_position + 1, end)
