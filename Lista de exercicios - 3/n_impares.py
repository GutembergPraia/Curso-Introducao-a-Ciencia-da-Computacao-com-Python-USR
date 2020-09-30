#   Exercício 2
#   Receba um número inteiro positivo na entrada e imprima os n primeiros números 
# ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
#
#   Exemplo:
#
#   Digite o valor de n: 5
#   1
#   3
#   5
#   7
#   9
#

i = int(input('Digite o valor de n: '))
j = 0
while not (i==0):
    if(j%2!=0):
        print(j)
        i -= 1
    j+=1
    
