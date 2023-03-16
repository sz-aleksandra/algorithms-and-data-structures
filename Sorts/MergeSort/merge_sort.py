
def merge(list_of_words):
    if len(list_of_words) > 1:
        half = len(list_of_words) // 2
        left_half = list_of_words[:half]
        right_half = list_of_words[half:]
        i, j = 0
        for word in list_of_words:
            if left_half[i] <= right_half[j]:
                word = left_half[i]
                i += 1
            else:
                word == right_half[j]
                j += 1
