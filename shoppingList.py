import os

lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        item = input('Item: ')
        lista.append(item)
    elif opcao == 'a':
        indice_str = input(
            'Escola o índice para apagar: '
    )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número int. (inteiro)')
        except IndexError:
            print('Esse índice não existe na lista.')
        except Exception:
            print('Erro desconhecido, entre em contato com o suporte em contato@contato.com.br')

    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada par listar')

        for i, valor in enumerate(lista):
            print(i, valor)

        else:
            print('Por favor, escola i, a ou l.')