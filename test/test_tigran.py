from src import tigran_modulation


def test_repeating_check():
    # Could be wrong, should get updated accordingly
    result = tigran_modulation.repeating_check(
        3, 4, 5, 3, 4, 5, 1, 1, 1, 2, 3, 2)

    assert result == False


# Considering adding more comprehensive tests here too,
# e.g. testing for other number combinations