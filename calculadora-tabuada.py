while True:
    n = int(input('Quer ver a tabuada de qual valor? \n'))
    if n == 0:
        break
    print('-=' * 30)
    for c in range(1,11):
       
        print(f'{n} X {c} = {n * c}')
    print('-=' * 30)
print('\033[34mPROGRAMA TABUADA ENCERRADO. Volte sempre! 😊👋🏻\033[m')