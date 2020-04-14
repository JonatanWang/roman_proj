import pytest

from src.roman.converts import int_to_roman


@pytest.fixture()
def sample_data():
    return 1


def test_sample_data(sample_data):
    assert int_to_roman(sample_data) == "I"