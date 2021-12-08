from helpers.add import add


def test_add_1():
    n, m = 4, 3

    result = add(n, m)

    assert result == 7


def test_add_2():
    n, m = 1, 1

    result = add(n, m)

    assert result == 2
