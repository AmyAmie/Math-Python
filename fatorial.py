n = int(input('Digite um número para calcular seu fatorial: \n'))
c = n
f = 1
print(f'Calculando {n}!  ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' X ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f'{f}.')
