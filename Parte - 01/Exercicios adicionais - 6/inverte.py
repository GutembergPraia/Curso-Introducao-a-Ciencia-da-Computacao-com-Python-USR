'''
    Exercício 2 - Invertendo sequência
 Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e 
 imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer
 parte da sequência.

Exemplo:
    Digite um número: 1
    Digite um número: 7
    Digite um número: 4
    Digite um número: 0

    4
    7
    1
'''

lista = []
while True:
    valor = int(input("Digite um número: "))
    if(valor>0):
        lista.append(valor)
    elif(valor == 0):
        print()
        break
lista = lista[::-1]
for i in range(len(lista)):
    print(lista[i])
    