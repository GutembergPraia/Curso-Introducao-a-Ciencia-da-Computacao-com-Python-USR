#   Exercício 1
#
#   Escreva um programa que receba um número inteiro positivo na entrada e verifique se 
# é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".
#
#   Exemplos:
#
#   Digite um número inteiro: 13
#   primo
#
#   Digite um número inteiro: 12
#   não primo
#

num  = int(input('Digite um número inteiro: '))
primo = True
contDiv = 0
i = 1

while (i<=num and primo):
    print(i)
    if(num % i == 0):
        contDiv += 1
        if(contDiv > 2):
            primo = False
    i += 1

if(primo):
    print('primo')
else:
    print('não primo')