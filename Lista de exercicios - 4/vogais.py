#                                   Exercício 3 - Vogais
#  Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e 
# False se for uma consoante.
# 
# Exemplos de execução no shell de Python
# 
# >>> vogal("a")
# True
# >>> vogal("b")
# False
# >>> vogal("E")
# True
#
def vogal(vogal:str):
    if(len(vogal)==1 and vogal.lower() in ['a','e','i','o','u']):
        return True
    else:
        return False
