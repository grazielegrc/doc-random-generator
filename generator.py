import enquiries
import generateAR
import generateBR
import generateCO
import generateDO
import generateEC
import generatePE


def chooseOption():
    countries = ['AR', 'BR', 'CO', 'DO', 'EC', 'PE']
    country = enquiries.choose('Choose the country: ', countries)
    if country == 'BR':
        typeDocument = enquiries.choose('Choose the type of document: ', ['CPF', 'CNPJ'])
        if typeDocument == 'CPF':
            print(f'CPF: {generateBR.generateCPF()}')
        if typeDocument == 'CNPJ':
            print(f'CNPJ: {generateBR.generateCNPJ()}')
    if country == 'CO':
        typeDocument = enquiries.choose('Choose the type of document: ',
                                        ['Persona Juridica - CI', 'Persona Juridica - NIT'])
        if typeDocument == 'Persona Juridica - CI':
            print(f'Persona Juridica - CI: {generateCO.generate_ci()}')
        if typeDocument == 'Persona Juridica - NIT':
            print(f'Persona Juridica - NIT: {generateCO.generate_nit()}')
    if country == 'DO':
        rnc_ci = enquiries.choose('Choose the type of document: ', ['RNC', 'CI'])
        if rnc_ci == 'RNC':
            print(f'RNC Persona Juridica: {generateDO.generate_rnc()}')
        if rnc_ci == 'CI':
            print(f'CI Persona Natural: {generateDO.generate_ci()}')
    if country == 'EC':
        ci_ruc = enquiries.choose('Choose the type of document: ', ['RUC', 'CI'])
        if ci_ruc == 'RUC':
            typePerson = enquiries.choose('Choose the type of person: ', ['Persona Natural', 'Persona Juridica'])
            if typePerson == 'Persona Natural':
                print(f'RUC Persona Natural: {generateEC.generateRUCPersonaNatural()}')
            if typePerson == 'Persona Juridica':
                print(f'RUC Persona Juridica: {generateEC.generateRUCPersonaJuridica()}')
        if ci_ruc == 'CI':
            print(f'CI: {generateEC.generateCedula()}')
    if country == 'PE':
        typeDocument = enquiries.choose('Choose the type of document: ', ['RUC', 'DNI'])
        if typeDocument == 'RUC':
            print(f'RUC: {generatePE.generateRUC()}')
        if typeDocument == 'DNI':
            print(f'DNI: {generatePE.generateDNI()}')
    if country == 'AR':
        print(f'CUIT: {generateAR.generate_cuit()}')


chooseOption()
