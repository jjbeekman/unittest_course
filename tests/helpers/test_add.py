from helpers.add import add
import pytest


@pytest.mark.parametrize("input,expected", [((4, 3), 7), ((1, 1), 2), ((1, 13), 14)])
def test_add_1(input, expected):
    n, m = input

    result = add(n, m)

    assert result == expected


def test_add_raises_assertion():
    n, m = -3, 2

    with pytest.raises(AssertionError):
        add(n, m)
