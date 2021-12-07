import advent.day7 as d7


def test_day_7_1():
    test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    result = d7.calc1(test_input)
    assert result == (2, 37)


def test_day_7_2():
    test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    result = d7.calc(test_input)
    assert result == (5, 168)
