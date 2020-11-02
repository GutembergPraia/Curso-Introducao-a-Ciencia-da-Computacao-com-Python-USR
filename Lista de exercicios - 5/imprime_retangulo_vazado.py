'''
    Exercício 2
    Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres 
 que não estiverem na borda do retângulo sejam espaços.

    Por exemplo:

    digite a largura: 10
    digite a altura: 3
    ##########
    #        #
    ##########

    digite a largura: 2
    digite a altura: 2
    ##
    ##

'''
def main():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a : "))
    i = altura
    while (i > 0):
        j = largura
        while(j > 0):
            if(i == altura or i == 1 or (i>1 and i<altura and (j==1 or j==largura))):
                print("#",end="")
            else:
                print(" ",end="")
            j -=1
        print()
        i -=1

main()