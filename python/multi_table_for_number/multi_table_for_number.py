def multi_table(multiplicando):
    tabla_de_multiplicar = ""
    UNO = 1
    DIEZ = 10
    for multiplicador in range(UNO, DIEZ +1):
        tabla_de_multiplicar += (
            f'{multiplicador} * {multiplicando} = {multiplicador * multiplicando}\n'
        )
    return tabla_de_multiplicar[:-1]
print(multi_table(5)) #<--- para debug