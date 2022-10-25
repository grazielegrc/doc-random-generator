import random


def generate_cuit():
    # precisa ser 20 (homem), 27 (mulher), 30 (empresas)
    firstDigit = [2, 3]
    one = random.choice(firstDigit)
    secDigit = [0, 7]
    two = random.choice(secDigit)
    while one == 3 and two != 0:
        one = random.choice(firstDigit)
        two = random.choice(secDigit)
    three_nine = random.sample(range(0, 9), 8)
    coefficient = [3, 2, 7, 6, 5, 4, 3, 2]
    mul1 = one * 5
    mul2 = two * 4
    s = sum(int(three_nine[i]) * coefficient[i] for i in range(8))
    sum_total = mul1 + mul2 + s
    div = sum_total % 11
    if div == 0:
        final_digit = 0
    elif div == 1:
        if one == 2 and two == 0:
            final_digit = 9
            one = 2
            two = 3
        if one == 2 and two == 7:
            final_digit = 4
            one = 2
            two = 3
    else:
        final_digit = 11 - div

    cuit_final = f'{one}, {two}, {three_nine}, {final_digit}'
    cuit_final_ = "".join(c for c in cuit_final if c.isdecimal())

    return cuit_final_
