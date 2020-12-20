div = 0
a = int(input('Digite um número: '))
for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div = div + 1

if div == 2:
    print (f'O número {a} é primo.')
else:
    print(f'O número {a} não é primo.')
