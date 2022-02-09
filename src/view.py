"""
This file is the 'view' of the program.
That is, it is concerned with how you can see program output.
"""


def print_values(a, b, c, d, e, f, m, n, o, x, y, z, count):
    print_generated_values(generate_print_line(
        a, b, c, d, e, f, m, n, o, x, y, z, count))


def generate_print_line(a, b, c, d, e, f, m, n, o, x, y, z, count) -> str:
    print_line = "Yeetus: a = " + str(a) + ", b = " + str(b) + ", c = " + str(c) + ", d = " + str(d) + ", e = " + str(e) + ", f = " + str(
        f) + ", m = " + str(m) + ", n = " + str(n) + ", o = " + str(o) + ", x = " + str(x) + ", y = " + str(y) + ", z = " + str(z) + ", count = " + str(count)

    return(print_line)


def print_generated_values(print_line: str):
    return print(print_line)
