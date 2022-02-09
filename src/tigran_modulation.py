from src.view import *


def repeating_check(a, b, c, d, e, f, m, n, o, x, y, z) -> bool:
    '''
    This function is the repeating boolean check in this script.
    I don't really know what it does so the names are generic.
    Should update the names as appropriate.
    '''

    check_one_name = m*a + n*b + o*c == (2**x)*z and m*d + n*e + o*f
    check_two_name = (1 < (a*e) / (b*d) <= 6/5 or 1 < (b*d) / (a*e) <= 6/5)
    check_three_name = (1 < (a*f) / (c*d) <= 6/5 or 1 < (c*d) / (a*f) <= 6/5)
    check_four_name = (1 < (b*f) / (c*e) <= 6/5 or 1 < (c*e) / (b*f) <= 6/5)
    check_five_name = a != d and b != e and c != f and a < b and b < c and d < e and e < f

    return check_one_name and check_two_name and check_three_name and check_four_name and check_five_name


def tigran_modulation():
    count = 0
    a = 3

    for i in range(5):
        b = 4
        for i in range(5):
            c = 5
            for i in range(5):
                d = 3
                for i in range(5):
                    e = 4
                    for i in range(5):
                        f = 5
                        for i in range(5):
                            m = 1
                            for i in range(7):
                                n = 1
                                for i in range(7):
                                    o = 1
                                    for i in range(7):
                                        x = 2
                                        for i in range(6):
                                            y = 3
                                            for i in range(4):
                                                z = 2
                                                for i in range(6):
                                                    if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
                                                        count += 1
                                                        print_values(
                                                            a, b, c, d, e, f, m, n, o, x, y, z, count)
                                                    z += 1
                                                if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
                                                    count += 1
                                                    print_values(
                                                        a, b, c, d, e, f, m, n, o, x, y, z, count)
                                                y += 1
                                            if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
                                                count += 1
                                                print_values(
                                                    a, b, c, d, e, f, m, n, o, x, y, z, count)
                                            x += 1
                                        if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
                                            count += 1
                                            print_values(
                                                a, b, c, d, e, f, m, n, o, x, y, z, count)
                                        o += 1
                                    if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
                                        count += 1
                                        print_values(
                                            a, b, c, d, e, f, m, n, o, x, y, z, count)
                                    n += 1
                                if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
                                    count += 1
                                    print_values(
                                        a, b, c, d, e, f, m, n, o, x, y, z, count)

                                m += 1
                            if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
                                count += 1
                                print_values(
                                    a, b, c, d, e, f, m, n, o, x, y, z, count)

                            f += 1
                        if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
                            count += 1
                            print_values(
                                a, b, c, d, e, f, m, n, o, x, y, z, count)

                        e += 1
                    if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
                        count += 1
                        print_values(
                            a, b, c, d, e, f, m, n, o, x, y, z, count)

                    d += 1
                if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
                    count += 1
                    print_values(
                        a, b, c, d, e, f, m, n, o, x, y, z, count)

                c += 1
            if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
                count += 1
                print_values(
                    a, b, c, d, e, f, m, n, o, x, y, z, count)

            b += 1
        if repeating_check(a, b, c, d, e, f, m, n, o, x, y, z):
            count += 1
            print_values(
                a, b, c, d, e, f, m, n, o, x, y, z, count)

        a += 1
