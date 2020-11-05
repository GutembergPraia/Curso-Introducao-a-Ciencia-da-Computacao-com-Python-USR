'''
    Exercício 2: Matrizes multiplicáveis
    Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao número de linhas da segunda. 
 Escreva a função sao_multiplicaveis(m1, m2) que recebe duas matrizes como parâmetro e devolve True se as matrizes 
 forem multiplicavéis (na ordem dada) e False caso contrário.

    Exemplos:

    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    sao_multiplicaveis(m1, m2) => False

    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    sao_multiplicaveis(m1, m2) => True

'''

def sao_multiplicaveis(m1, m2):
    m1_colunas = 0
    for m1_linha in m1:
        if(m1_colunas<len(m1_linha)):
            m1_colunas = len(m1_linha)
            
    m2_linhas = len(m2) 
    
    
    if(m1_colunas == m2_linhas):
        return True
    else:
        return False
