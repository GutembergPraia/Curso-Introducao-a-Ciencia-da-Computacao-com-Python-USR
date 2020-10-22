#                           Exercício 2 - Primos
#   Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 
# como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
# 
# Exemplos de execução no shell do Python:
# 
# >>> maior_primo(100)
# 97
# >>> maior_primo(7)
# 7

def ePrimo(num:int):
  primo = True
  i = 0
  cont = 0
  while(i<num and primo):
    i+=1
    if(num%i==0):
      cont+=1
    if cont > 2:
      primo = False
    
  return primo

def maior_primo(num:int):
  i = num
  while(i>=2):
    if(ePrimo(i)):
      return i
    else:
      i-=1
  return 2