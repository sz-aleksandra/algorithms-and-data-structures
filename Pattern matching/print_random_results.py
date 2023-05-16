import random
import string
from kr_algorithm import find_KR
from kmp_algorithm import find_KMP
from Naive_algorithm import find_N


def test_string_matching_algorithms():
    LETTERS = [random.choice(string.ascii_letters), random.choice(string.ascii_letters)]
    NUMBER_OF_TESTS = 10
    MAX_TEXT_LENGTH = 100
    MAX_PATTERN_LENGTH = 10

    for _ in range(NUMBER_OF_TESTS):
        text_length = random.randint(1, MAX_TEXT_LENGTH)
        pattern_length = random.randint(1, min(text_length, MAX_PATTERN_LENGTH))

        text = ''.join(random.choices(LETTERS, k=text_length))
        pattern = ''.join(random.choices(LETTERS, k=pattern_length))

        kr_result = find_KR(pattern, text)
        kmp_result = find_KMP(pattern, text)
        naive_result = find_N(pattern, text)

        print(f"Text: {text}")
        print(f"Pattern: {pattern}")

        assert kr_result == kmp_result == naive_result, \
            "The algorithms returned different results!"

        print(f"KR algorithm returned: {kr_result}\n")
        print(f"KMP algorithm returned: {kmp_result}\n")
        print(f"NAIVE algorithm returned: {naive_result}\n")


if __name__ == "__main__":
    test_string_matching_algorithms()
