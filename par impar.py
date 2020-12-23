print("\033[34mOlá, eu \033[0;34msou o \033[1;34mseu\033[0;34m computador")
prompt = int(input("\033[34mDigite \033[1m um\033[m \033[34m número para eu ve-lo se ele é \033[1;34mpar\033[0;34m ou \033[1;34mímpar\033[m: \033[0;34m\n"))
if prompt % 2 == 0:
    print("\033[34mO número que você digitou foi \033[1mPAR\033[0;34m!")
else:
    print("\033[34mO número que você digitou foi \033[1;34mÍMPAR\033[0;34m!")
