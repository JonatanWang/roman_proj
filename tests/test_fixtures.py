import pytest

from src.roman.converts import int_to_roman


@pytest.fixture()
def sample_data():
    return 1


@pytest.fixture()
def a_group_sample_data():
    return [1,5,15,42,9,94,1776]


@pytest.fixture()
def test_sample_data(sample_data):
    assert int_to_roman(sample_data) == "I"


def test_a_group_sample_data(a_group_sample_data):
    expected = [ "I",  "V",  "XV", "XLII", "IX", "XCIV", "MDCCLXXVI"]
    for i in range(len(a_group_sample_data)):
        assert int_to_roman(a_group_sample_data[i]) == expected[i]