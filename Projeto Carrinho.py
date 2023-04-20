from time import sleep
produtos = ['Tecido', 'Linhas e Agulhas', 'Maquina de Costura', 'Ferramentas de Reparo', 'Tecidos especiais e Linhas Premium',]
carrinho = []
cont = 0

#Bem Vindo
print('-='*22)
print(f'{"Bem vindo a lojinha do seu Augusto":^44}')
print('-='*22)
sleep(1)

#Looping
while True:
    if cont >= 1:
        comandoparar = int(input('Você quer continuar comprando? \n[1] Sim [Qualquer valor] Não: '))
        if comandoparar != 1:
            print('Obrigado por ter comprado com a gente!')
            print(f'O seu carrinho foi: {carrinho}')
            print('-=' * 22)
            break
    comando = int(input('Olá o que você vai comprar?'
                        '\n[1] Tecido \n[2] Kit de Agulhas \n[3] Maquina de Costura '
                        '\n[4] Ferramentas de Reparo \n[5] Kit Premium \nDigite o Valor: '))
    print('-=' * 22)

    #Erro de digitação comando1
    while comando not in [1, 2, 3, 4, 5]:
        print('O valor inserido não existe tente novamente:')
        sleep(0.5)
        comando = int(input('Olá o que você vai comprar?'
                            '\n[1] Tecido \n[2] Kit de Agulhas \n[3] Maquina de Costura '
                            '\n[4] Ferramentas de Reparo \n[5] Kit Premium \nDigite o Valor: '))
        print('-=' * 22)
        sleep(0.5)
    sleep(0.5)
    carrinho.append(produtos[comando - 1])
    cont += 1

    #Comando2
    comando2 = int(input('Continuar comprando [0] \nVer carrinho [1] \nParar a compra [2] \nDigite o valor: '))
    print('-=' * 22)
    sleep(1)
    #Comprar
    if comando2 == 0:
        pass

    #Carrinho
    elif comando2 == 1:
        print(carrinho)
        sleep(1)
        #Alteração da compra
        comando3 = int(input('Você gostaria de alterar algum produto?\n[0] Sim \n[Qualquer valor] Não \nDigite o valor: '))
        print('-=' * 22)
        if comando3 == 0:
            remocao = int(input('Qual o número do item na lista que você quer retirar? '))
            print('-=' * 22)

            # Erro de digitação remocao
            if remocao > (len(carrinho) + 1):
                while remocao > (len(carrinho) + 1):
                    print('Esse valor não existe, tente novamente: ')
                    sleep(0.5)
                    remocao = int(input('Qual o número do item na lista que você quer retirar? '))
                    print('-=' * 22)
                    if remocao <= (len(carrinho) + 1):
                        carrinho.pop(remocao - 1)
            else:
                carrinho.pop(remocao - 1)
        else:
            pass

    #Parar Compra
    elif comando2 == 2:
        print('Obrigado por ter comprado com a gente!')
        print(f'O seu carrinho foi: {carrinho}')
        print('-=' * 22)
        break

    #Erro de digitação comando2
    else:
        while comando2 not in [0, 1, 2]:
            print('O valor inserido não existe tente novamente: ')
            sleep(0.5)
            comando2 = int(input('Continuar comprando [0] \nVer carrinho [1] \nParar a compra [2] \nDigite o valor: '))
            print('-=' * 22)
            sleep(1)
            #Compra
            if comando2 == 0:
                pass

            #Ver Carrinho
            elif comando2 == 1:
                print(carrinho)
                sleep(1)
                # Alteração da compra
                comando3 = int(
                    input('Você gostaria de alterar algum produto?\n[0] Sim \n[Qualquer valor] Não \nDigite o valor: '))
                print('-=' * 22)
                if comando3 == 0:
                    remocao = int(input('Qual o número do item na lista que você quer retirar? '))
                    print('-=' * 22)

                    #Erro de digitação remocao
                    if remocao > (len(carrinho)) + 1:
                        while remocao > (len(carrinho) + 1):
                            print('Esse valor não existe, tente novamente: ')
                            sleep(0.5)
                            remocao = int(input('Qual o número do item na lista que você quer retirar? '))
                            print('-=' * 22)
                            if remocao <= (len(carrinho) + 1):
                                carrinho.pop(remocao - 1)
                    else:
                        carrinho.pop(remocao - 1)

                else:
                    pass

            #Finalização
            elif comando2 == 2:
                print('Obrigado por ter comprado com a gente!')
                print(f'O seu carrinho foi: {carrinho}')
                print('-=' * 22)
                break