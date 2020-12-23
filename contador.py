from time import sleep
from sys import exit
def contador(i, f , p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        count = i
        while count <= f:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count += p
        print('FIM!')
    else:
        count = i
        while count >= f:
            print(f'`{count} ', end='', flush=True)
            sleep(0.5)
            count -= p
        print('FIM!')
print('Olá, eu sou o seu computador, e eu estou aqui para poder contar para você!')
ini = int(input('Início:    \n'))
fim = int(input('Fim:       \n'))
pas = int(input('Passo      \n'))
contador(ini,fim,pas)
