#   Exercício 1 - Par ou ímpar?
#   Receba um número inteiro na entrada e imprima
#   
#   par
#   
#   quando o número for par ou
#   
#   ímpar
#   
#   quando o número for ímpar.

num = int(input("Digite um número inteiro: "))
if(num == 0):
  print("Neutro")
else:
  if( num % 2 ):
    print("ímpar")
  else:
    print("par")