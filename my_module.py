import math


def sqrt(n, one):
    """
    Calculate the square root of an integer, with the precision passed in as
    one.
    This algorithm uses a second order Newton-Raphson convergence.
    """
    floating_point_precision = 10 ** 16
    n_float = float((n * floating_point_precision) // one) / \
              floating_point_precision
    x = (int(floating_point_precision * math.sqrt(n_float)) * one) // \
        floating_point_precision
    n_one = n * one
    while True:
        x_old = x
        x = (x + n_one // x) // 2
        if x == x_old:
            break
    return x


def pi_chudnovksy(one):
    """
    Calculate pi using a Chudnovksy's series.
    This calculates it in fixed point, using the precision passed in.
    """
    k = 1
    a_k = one
    a_tot = one
    b_tot = 0
    C = 640320
    C3_OVER_24 = C ** 3 // 24
    while True:
        a_k *= -(6 * k - 5) * (2 * k - 1) * (6 * k - 1)
        a_k //= k ** 3 * C3_OVER_24
        a_tot += a_k
        b_tot += k * a_k
        k += 1
        if a_k == 0:
            break
    total = 13591409 * a_tot + 545140134 * b_tot
    pi = (426880 * sqrt(10005 * one, one) * one) // total
    return pi


def validate_nonnegative_integer():
    """
    Ask the user for input and only return when a nonnegative integer under
    10000 is given.
    """
    while True:
        s = input("How many digits of pi do you want to see? ")
        try:
            digits = int(s)
            if digits >= 10000:
                print("Enter a number smaller than 10000.")
            elif digits > 0:
                return digits
            else:
                print("Enter a nonnegative integer.")

        except ValueError:
            print("Enter a nonnegative integer.")


def main():
    digits = validate_nonnegative_integer()
    pi = str(pi_chudnovksy(10 ** (digits * 10)))[:digits]
    print(pi[0] + "." + pi[1:])


# Обменник
def nominals(summa):
    a = {
        "100 000 $": 0,
        "50 000 $": 0,
        "10 000 $": 0,
        "5 000 $": 0,
        "1 000 $": 0,
        "500 $": 0,
        "100 $": 0,
        "50 $": 0,
        "10 $": 0,
        "5 $": 0,
        "1 $": 0,
        "50 C": 0,
        "25 C": 0,
        "10 C": 0,
        "5 C": 0,
        "1 C": 0
    }

    while True:
        if summa > 100000:
            summa -= 100000
            a["100 000 $"] += 1
            continue

        if summa > 50000:
            summa -= 50000
            a["50 000 $"] += 1
            continue

        if summa > 10000:
            summa -= 10000
            a["10 000 $"] += 1
            continue

        if summa > 5000:
            summa -= 5000
            a["5 000 $"] += 1
            continue

        if summa > 1000:
            summa -= 1000
            a["1 000 $"] += 1
            continue

        if summa > 500:
            summa -= 500
            a["500 $"] += 1
            continue

        if summa > 100:
            summa -= 100
            a["100 $"] += 1
            continue

        if summa > 50:
            summa -= 50
            a["50 $"] += 1
            continue

        if summa > 10:
            summa -= 10
            a["10 $"] += 1
            continue

        if summa > 5:
            summa -= 5
            a["5 $"] += 1
            continue

        if summa > 1:
            summa -= 1
            a["1 $"] += 1
            continue

        if summa > 0.5:
            summa -= 0.5
            a["50 C"] += 1
            continue

        if summa > 0.25:
            summa -= 0.25
            a["25 C"] += 1
            continue

        if summa > 0.10:
            summa -= 0.10
            a["10 C"] += 1
            continue

        if summa > 0.05:
            summa -= 0.05
            a["5 C"] += 1
            continue

        if summa > 0.01:
            summa -= 0.01
            a["1 C"] += 1
            continue

        return a
