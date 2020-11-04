'''
    Exercício 1: Tamanho da matriz
    Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as 
 dimensões da matriz recebida, no formato iXj.

Exemplos:
    minha_matriz = [[1], [2], [3]]
    dimensoes(minha_matriz)
    3X1

    minha_matriz = [[1, 2, 3], [4, 5, 6]]
    dimensoes(minha_matriz)
    2X3

'''

def dimensoes(mat):
    linha = len(mat)
    coluna = 0
    for lin in mat:
        if(coluna < len(lin)):
            coluna = len(lin)
    
    
    print(str(linha)+"X"+str(coluna))