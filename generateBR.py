import random
import string


def generateCPF():
    cpf_initial = random.sample(range(0, 9), 9)
    coefficient_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    sum1_total = sum(int(cpf_initial[i]) * coefficient_1[i] for i in range(9))
    first_module = sum1_total % 11
    first_dv = 11 - first_module
    if first_dv > 9:
        first_dv = 0
    coefficient_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3]
    sum2_total = sum(int(cpf_initial[i]) * coefficient_2[i] for i in range(9)) + first_dv * 2
    sec_module = sum2_total % 11
    sec_dv = 11 - sec_module
    if sec_dv > 9:
        sec_dv = 0
    cpf_final_ = f'{cpf_initial}{first_dv}{sec_dv}'
    cpf_final = "".join(c for c in cpf_final_ if c.isdecimal())
    return cpf_final


def generateCNPJ():
    x = string.digits
    v = 12
    cnpj_initial = ''.join([random.choice(x) for _ in range(v)])
    coefficient_1 = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    sum1_total = sum(int(cnpj_initial[11 - i]) * coefficient_1[i] for i in range(12))
    first_module = sum1_total % 11
    first_dv = 11 - first_module
    if first_dv > 9:
        first_dv = 0
    coefficient_2 = [3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
    sum2_total = sum(int(cnpj_initial[11 - i]) * coefficient_2[i] for i in range(12)) + first_dv * 2
    sec_module = sum2_total % 11
    sec_dv = 11 - sec_module
    if sec_dv > 9:
        sec_dv = 0
    cnpj_final_ = f'{cnpj_initial}{first_dv}{sec_dv}'
    cnpj_final = "".join(c for c in cnpj_final_ if c.isdecimal())
    return cnpj_final
