import pytest


@pytest.fixture
def sample_list():
    return ['a', 'b', 'c', 'd', 'E', 'A', 'Abecadło',
            '123', '1', '0', 'Litwo', 'Pan', 'Tadeusz', 'Mickiewicz']
