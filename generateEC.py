import random


def generateCedula():
    coefficient = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    province_1 = random.randint(0, 3)
    province_2 = random.randint(0, 9)
    while province_1 == 2 and province_2 > 4 or province_1 == 3 and province_2 != 0 \
            or province_1 == 0 and province_2 == 0:
        province_1 = random.randint(0, 3)
        province_2 = random.randint(0, 9)
    third_digit = random.randint(0, 5)
    four_nine = random.sample(range(0, 10), 6)
    ci_initial = [province_1, province_2, third_digit]
    ci_initial.extend(four_nine)

    sum_total = 0
    for i in range(9):
        result = ci_initial[i] * coefficient[i]
        if result > 9:
            result = result - 9
        sum_total += result

    ci_initial = ''.join(str(i) for i in ci_initial)
    module = sum_total % 10
    if module == 0:
        final_digit = 0
    else:
        final_digit = 10 - module
    ci_final = f'{ci_initial}{final_digit}'

    return ci_final


def generateRUCPersonaNatural():
    ruc = generateCedula()
    return ruc


def generateRUCPersonaJuridica():
    province_1 = random.randint(0, 3)
    province_2 = random.randint(0, 9)
    while province_1 == 2 and province_2 > 4 or province_1 == 3 and province_2 != 0 \
            or province_1 == 0 and province_2 == 0:
        province_1 = random.randint(0, 3)
        province_2 = random.randint(0, 9)
    thirdDigit = [6, 9]
    three = random.choice(thirdDigit)
    four = random.randint(0, 9)
    five = random.randint(0, 9)
    six = random.randint(0, 9)
    seven = random.randint(0, 9)
    eight = random.randint(0, 9)
    nine = random.randint(0, 9)

    if three == 9:
        mul1 = province_1 * 4
        mul2 = province_2 * 3
        mul3 = three * 2
        mul4 = four * 7
        mul5 = five * 6
        mul6 = six * 5
        mul7 = seven * 4
        mul8 = eight * 3
        mul9 = nine * 2

        sum_total = mul1 + mul2 + mul3 + mul4 + mul5 + mul6 + mul7 + mul8 + mul9
        module = sum_total % 11
        if module > 1:
            final_digit = 11 - module
        else:
            final_digit = 0

        ruc_final = f'{province_1}{province_2}{three}{four}{five}{six}{seven}{eight}{nine}{final_digit}001'

    if three == 6:
        mul1 = province_1 * 3
        mul2 = province_2 * 2
        mul3 = three * 7
        mul4 = four * 6
        mul5 = five * 5
        mul6 = six * 4
        mul7 = seven * 3
        mul8 = eight * 2
        sum_total = mul1 + mul2 + mul3 + mul4 + mul5 + mul6 + mul7 + mul8
        module = sum_total % 11
        if module > 1:
            final_digit = 11 - module
        else:
            final_digit = 0

        ruc_final = f'{province_1}{province_2}{three}{four}{five}{six}{seven}{eight}{final_digit}0001'

    return ruc_final



