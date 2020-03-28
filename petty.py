from random import randint as r
import msvcrt as m

while True:
    try:
        text = ''
        run = True
        print(">> ", end='')
        while run:
            t = input()
            if t != "yes":
                text += t + '\n'
            else:
                run = False
        print('-'*50)
        p = ''
        c = 0
        for i in text:
            n = r(0, 1)
            c += 1 if n == 1 else -1
            c, n = (0, 0) if c >= 2 else (c, n)
            c, n = (0, 1) if c <= -2 else (c, n)
            p += i.upper() if n == 1 else i.lower()
        print(f'\n{p}\n')

    except(KeyboardInterrupt):
        exit(0)
