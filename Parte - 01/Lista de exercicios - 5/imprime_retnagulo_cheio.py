'''
    Exercício 1
 
    Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros 
 correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir 
 uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

    Por exemplo:

    digite a largura: 10
    digite a altura: 3
    ##########
    ##########
    ##########

    digite a largura: 2
    digite a altura: 2
    ##
    ##

    Dica: lembre-se que a função print pode receber um parametro 'end', que altera o último 
 caractere da cadeia, tornando possível a remoção da quebra de linha (reveja as vídeo-aulas)

'''
def main():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    while (altura > 0):
        i = largura
        while(i > 0):
            print("#",end="")
            i -=1
        print()
        altura -=1

main()