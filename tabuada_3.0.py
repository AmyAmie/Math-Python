def msg(a):
    print(f'{(len(a))*"--"}\n  {  a}\n{(len(a))*"--"}')

total = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor?   \n'))
    if n == 0:
        break
    print('-=' * 10)
    for c in range(1,11):
        total += 1

        print(f'{n} X {c} = {n * c}')
    print('-=' * 10)
print(f'PROGRAMA TABUADA ENCERRADO COM {total} MULTIPLICAÇÕES MOSTRADAS. Volte sempre!')