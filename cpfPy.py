import os

cpfEnviadoUsuario = input('Digite seu CPF abaixo. (Apenas números)\n')
noveDigitos = cpfEnviadoUsuario[:9]
contadorRegressivo1 = 10

try:
    resultadoDigito1 = 0
    for digito in noveDigitos:
        resultadoDigito1 += (int(digito) * contadorRegressivo1)
        contadorRegressivo1 -= 1
    digito1 = ((resultadoDigito1 * 10) % 11)
    digito1 = digito1 if digito1 <= 9 else 0

    dezDigitos = noveDigitos + str(digito1)
    contadorRegressivo2 = 11

    resultadoDigito2 = 0
    for digito in dezDigitos:
        resultadoDigito2 += int(digito) * contadorRegressivo2
        contadorRegressivo2 -= 1
    digito2 = ((resultadoDigito2 * 10) % 11)
    digito2 = digito2 if digito2 <= 9 else 0

    cpfGeradoCalculo = (f'{noveDigitos}{digito1}{digito2}')

    if cpfEnviadoUsuario == cpfGeradoCalculo:
        print(f'{cpfEnviadoUsuario} é válido')
    else:
        print('CPF inválido')
    
except ValueError:
    os.system('cls')
    print(f'Digite apenas números, sem "." ou "-"')
