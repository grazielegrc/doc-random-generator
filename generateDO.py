import random
import string

"""
A cedula is is an 11-digit number issues by the Dominican Republic government
to citizens or residents for identification purposes.
"""

def generate_ci():
    ci_initial = random.sample(range(0, 10), 10)
    ci_initial = ''.join(str(i) for i in ci_initial)
    while int(ci_initial[0:3]) != 402 and 121 < int(ci_initial[0:3]) < 1:
        ci_initial = random.sample(range(0, 10), 10)
    ci_initial = ''.join(str(i) for i in ci_initial)
    digits = list(map(int, ci_initial))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    module = (odd_sum + even_sum) % 10
    final_digit = (10 - module) % 10

    ci_final = f'{ci_initial}{final_digit}'

    return ci_final

"""
The RNC is the Dominican Republic taxpayer registration number for
institutions. The number consists of 9 digits.
"""

def generate_rnc():
    rnc_initial = random.sample(range(0, 10), 8)
    rnc_initial = ''.join(str(i) for i in rnc_initial)
    while int(rnc_initial[0]) != 1 and int(rnc_initial[0]) != 4 and int(rnc_initial[0]) != 5:
        rnc_initial = random.sample(range(0, 10), 8)
    rnc_initial = ''.join(str(i) for i in rnc_initial)
    coefficient = [7, 9, 8, 6, 5, 4, 3, 2]
    s = sum(int(rnc_initial[i]) * coefficient[i] for i in range(8)) % 11
    if s == 0:
        final_digit = 2
    elif s == 1:
        final_digit = 1
    else:
        final_digit = 11 - s
    rnc_final = f'{rnc_initial}{final_digit}'

    return rnc_final

