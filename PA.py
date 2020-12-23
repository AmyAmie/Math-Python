print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: \n'))
razão = int(input('Razão da PA: \n'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} => ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? \n'))
print(f'Programa finalizado com \033[1m{total}\033[m termos mostrados.')