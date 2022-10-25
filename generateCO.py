import random


def generate_nit():
    nit_initial = random.sample(range(0, 10), 9)
    coefficient = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]
    nit_initial = ''.join(str(i) for i in nit_initial)
    s = sum(int(nit_initial[8 - i]) * coefficient[i] for i in range(9)) % 11
    if s > 1:
        final_digit = 11 - s
    else:
        final_digit = s
    nit_final = f'{nit_initial}{final_digit}'

    return nit_final


def generate_ci():
    ci_initial = random.randint(00000000, 9999999999)
    coefficient = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]
    ci_initial = str(ci_initial)
    l = len(ci_initial) - 1
    s = sum(int(ci_initial[l - i]) * coefficient[i] for i in range(l+1)) % 11
    if s > 1:
        final_digit = 11 - s
    else:
        final_digit = s
    ci_final = f'{ci_initial}{final_digit}'

    return ci_final

