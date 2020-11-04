'''
    Exercício 2: Soma de matrizes
    Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que represente sua 
 soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

    Exemplos:

    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    soma_matrizes(m1, m2) => [[3, 5, 7], [9, 11, 13]]

    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    soma_matrizes(m1, m2) => False
'''

def dimensoes(mat):
    linha = len(mat)
    coluna = 0
    for lin in mat:
        if(coluna < len(lin)):
            coluna = len(lin)
    
    return [linha,coluna]    

def soma_matrizes(m1, m2):
    m1_lin_x_col = dimensoes(m1)
    m2_lin_x_col = dimensoes(m2)

    
    if(m1_lin_x_col == m2_lin_x_col):
        soma = []
        for i in range(m1_lin_x_col[0]):
            soma.append([])
            for j in range(m1_lin_x_col[1]):
                soma[i].append(m1[i][j]+ m2[i][j])

        return soma
    else:
        return False