
def merge(list_of_words):
    if len(list_of_words) > 1:

        half = len(list_of_words) // 2
        left_half = list_of_words[:half]
        right_half = list_of_words[half:]

        left_index = right_index = list_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                list_of_words[list_index] = left_half[left_index]
                left_index += 1

            else:
                list_of_words[list_index] = right_half[right_index]
                right_index += 1
            list_index += 1

        while left_index < len(left_half):
            list_of_words[list_index] = left_half[left_index]
            list_index += 1
            left_index += 1

        while right_index < len(right_half):
            list_of_words[list_index] = right_half[right_index]
            list_index += 1
            right_index += 1


