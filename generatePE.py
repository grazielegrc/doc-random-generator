import random


def generateRUC():
    # precisa começar com 10, 15, 16, 17 ou 20
    firstDigit = [1, 2]
    one = random.choice(firstDigit)
    secDigit = [0, 5, 6, 7]
    two = random.choice(secDigit)
    while one == 2 and two != 0:
        one = random.choice(firstDigit)
        two = random.choice(secDigit)
    three_nine = random.sample(range(0, 9), 8)
    coefficient = [3, 2, 7, 6, 5, 4, 3, 2]
    mul1 = one * 5
    mul2 = two * 4
    s = sum(int(three_nine[i]) * coefficient[i] for i in range(8))
    sum_total = mul1 + mul2 + s
    div = sum_total // 11

    sub = 11 - (sum_total - div*11)
    if sub == 10:
        final_digit = 0
    elif sub == 11:
        final_digit = 1
    else:
        final_digit = sub
    ruc_final = f'{one}, {two}, {three_nine}, {final_digit}'
    ruc_final_ = "".join(c for c in ruc_final if c.isdecimal())

    return ruc_final_


def generateDNI():

    numbers = (6, 7, 8, 9, 0, 1, 1, 2, 3, 4, 5)
    letters = ('K', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
    coefficient = (3, 2, 7, 6, 5, 4, 3, 2)

    dni = str(random.randint(1000000, 99999999)).zfill(8)

    dni = str(dni).replace('-', '').replace('.', '').strip().upper()
    numdni = [*map(int, dni[:8])]
    dsum = sum([x * y for x, y in [*zip(coefficient, numdni)]])
    key = 11 - (dsum % 11)
    if key == 11:
        key = 0
    dv_number = numbers[key]
    dv_letter = letters[key]

    return {
        'numeric': dni + str(dv_number),
        'letter': dni + dv_letter
    }
