from Naive_algorithm import find_N, find_KMP
from kr_algorithm import find_KR


def test_find_N_empty_string():
    positions = find_N('', 'Ciekawy wyjazd z przyjaciolmi')
    assert positions == []


def test_find_N_empty_string_and_text():
    positions = find_N('', '')
    assert positions == []


def test_find_N_string_equal_to_text():
    positions = find_N('Ciekawy wyjazd', 'Ciekawy wyjazd')
    assert positions == [0]


def test_find_N_string_longer_than_text():
    positions = find_N('Ciekawy wyjazd z przyjaciolmi', 'Ciekawy wyjazd')
    assert positions == []


def test_find_N_string_not_in_text():
    positions = find_N('dasmdkasmdka', 'Ciekawy wyjazd z przyjaciolmi')
    assert positions == []


def test_find_KMP_empty_string():
    positions = find_KMP('', 'Ciekawy wyjazd z przyjaciolmi')
    assert positions == []


def test_find_KMP_empty_string_and_text():
    positions = find_KMP('', '')
    assert positions == []


def test_find_KMP_string_equal_to_text():
    positions = find_KMP('Ciekawy wyjazd', 'Ciekawy wyjazd')
    assert positions == [0]


def test_find_KMP_string_longer_than_text():
    positions = find_KMP('Ciekawy wyjazd z przyjaciolmi', 'Ciekawy wyjazd')
    assert positions == []


def test_find_KMP_string_not_in_text():
    positions = find_KMP('admaskldmdasda', 'Ciekawy wyjazd z przyjaciolmi')
    assert positions == []


def test_find_KR_empty_string():
    positions = find_KR('', 'Ciekawy wyjazd z przyjaciolmi')
    assert positions == []


def test_find_KR_empty_string_and_text():
    positions = find_KR('', '')
    assert positions == []


def test_find_KR_string_equal_to_text():
    positions = find_KR('Ciekawy wyjazd', 'Ciekawy wyjazd')
    assert positions == [0]


def test_find_KR_string_longer_than_text():
    positions = find_KR('Ciekawy wyjazd z przyjaciolmi', 'Ciekawy wyjazd')
    assert positions == []


def test_find_KR_string_not_in_text():
    positions = find_KR('admaskldmdasda', 'Ciekawy wyjazd z przyjaciolmi')
    assert positions == []
