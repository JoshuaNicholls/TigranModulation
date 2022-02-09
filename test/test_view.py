from src import view


# Update with realistic input values
def test_view():
    result = view.generate_print_line(
        'a', 'b', 'c', 'd', 'e', 'f', 'm', 'n', 'o', 'x', 'y', 'z', 'count')

    expected = "Yeetus: a = a, b = b, c = c, d = d, e = e, f = f, m = m, n = n, o = o, x = x, y = y, z = z, count = count"

    assert result == expected
