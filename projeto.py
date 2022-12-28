from time import sleep
from random import randint
while True:
    start = str(input('Começar[S/N]:')).upper()
    if start == 'S':
        jogos = str(input('[0] = Sair\n'
                      '[1] = Suc e ant\n'
                      '[2] = Calculos\n'
                      '[3] = Média\n'
                      '[4] = Conversor\n'
                      '[5] = Tabuada\n'
                      '[6] = Dolar\n'
                      '[7] = Jokenpô\n'
                      'Escolha uma função:'))
        if jogos == '0':
            print('Finalizando...')
            sleep(1)
            break
        if jogos == '1':
            while True:
                numero = int(input('Digite um numero para saber seu sucessor e seu antecessor:'))
                print(f'O numero escolhido foi o {numero}\n'
                    f'Seu sucessor é o {numero+1}\n'
                    f'Seu antecessor é o {numero-1}')
                ag = str(input('Quer jogar novamente?[S/N]:')).upper()
                if ag == 'N':
                    break
                elif ag == 'S':
                    print('Recomeçando...')
                    sleep(1)
        elif jogos == '2':
            while True:
                numero = int(input('Digite um numero para saber seu dobro seu triplo e sua raiz:'))
                print(f'Seu do dobro é {numero * 2}\n'
                      f'Seu triplo é {numero * 3}\n'
                      f'E sua raiz quadrada é {numero ** (1 / 2)}')
                ag = str(input('Quer jogar novamente?[S/N]:')).upper()
                if ag == 'N':
                    break
                elif ag == 'S':
                    print('Recomeçando...')
                    sleep(1)
        elif jogos == '3':
            while True:
                n1 = int(input('Digite o primeiro valor para a média:'))
                n2=int(input('Digite o segundo valor:'))
                print(f'A média de {n1} + {n2} é de {(n1 + n2)/2}')
                ag = str(input('Quer jogar novamente?[S/N]:')).upper()
                if ag == 'N':
                    break
                elif ag == 'S':
                    print('Recomeçando...')
                    sleep(1)
        elif jogos == '4':
            while True:
                metros=float(input('Quantos metros precisa converter?'))
                print(f'{metros} metros equivale a {metros*100} centimetros e {metros*1000} miniletros')
                ag = str(input('Quer jogar novamente?[S/N]:')).upper()
                if ag == 'N':
                    break
                elif ag == 'S':
                    print('Recomeçando...')
                    sleep(1)
        elif jogos == '5':
            while True:
                tabuada=int(input('Digite um numero e para descobrir sua tabuada:'))
                print('-_'*6)
                for c in range(1,11):
                    print(f'{tabuada} * {c} = {tabuada*c}')
                print('-_'*6)
                ag = str(input('Quer jogar novamente?[S/N]:')).upper()
                if ag == 'N':
                    break
                elif ag == 'S':
                    print('Recomeçando...')
                    sleep(1)
        elif jogos == '6':
            while True:
                dolar=float(input('Quantos reais você possui? R$:'))
                print(f'Com R$:{dolar} você consegue comprar U$:{dolar/3.27} dolares')
                ag = str(input('Quer jogar novamente?[S/N]:')).upper()
                if ag == 'N':
                    break
                elif ag == 'S':
                    print('Recomeçando...')
                    sleep(1)
        elif jogos == '7':
            while True:
               pc=randint(1,3)
               escolha=str(input('[1] Pedra\n'
                        '[2] Papel\n'
                        '[3] Tesoura\n'
                        ':'))
               sleep(0.5)
               print('JO')
               sleep(0.5)
               print('KEN')
               sleep(0.5)
               print('PÔ')
               print(pc)
               if escolha!='1' and escolha!='2' and escolha!='3':
                   print('ERRO!!!')
               elif escolha == '1':
                    print('Você:Pedra!!')
                    if pc == 2:
                        print('Computador:Papel!!\nVOCÊ PERDEU')
                    elif pc == 3:
                        print('Computador:Tesoura!!\nVOCÊ GANHOU')
                    elif pc == 1:
                        print('Computador:Pedra!!')
                        print('Empatou!')
               elif escolha == '2':
                    print('Você:Papel!!')
                    if pc == 1:
                        print('Computador:Pedra!!\nVOCÊ GANHOU')
                    elif pc == 3:
                        print('Computador:Tesoura!!\nVOCÊ PERDEU')
                    elif pc == 2:
                        print('Computador:Papel!!')
                        print('Empatou!')
               elif escolha == '3':
                   print('Você:Tesoura!!')
                   if pc == 1:
                       print('Computador:Pedra!!\nVOCÊ PERDEU')
                   elif pc == 2:
                       print('Computador:Papel!!\nVOCÊ GANHOU')
                   elif pc == 3:
                        print('Computador:Tesoura!!')
                        print('Empatou!')
               ag=str(input('Quer jogar novamente?[S/N]:')).upper()
               if ag =='N':
                   break
               elif ag == 'S':
                    print('Recomeçando...')
                    sleep(1)
        else:
            print('Não entendi!')
            sleep(1)
            novo = str(input('Buscar jogos?[S/N]')).upper()
            if novo == 'N':
                print('Finalizando...')
                sleep(1)
                break
            elif novo == 'S':
                print('Recomeçando...')
                sleep(1)
            elif novo != 'S' and novo != 'N':
                print('ERRO!')
                break
    elif start == 'N':
        print('Finalizando...')
        sleep(1)
        break