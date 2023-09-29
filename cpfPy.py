cpf = '21512449032'
noveDigitos = cpf[:9]
contadorRegressivo1 = 10

resultadoDigito1 = 0
for digito1 in noveDigitos:
    resultadoDigito1 += (int(digito1) * contadorRegressivo1)
    contadorRegressivo1 -= 1
digito1 = ((resultadoDigito1 * 10) % 11)
digito1 = digito1 if digito1 <= 9 else 0
print(digito1)