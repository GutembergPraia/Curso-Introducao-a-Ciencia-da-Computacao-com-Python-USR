#
#   Exercício 2 - Desafio do vídeo "Repetição com while"
#   
#   Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui 
# ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, 
# imprima "não".
#
#   Exemplos:
#
# Digite um número inteiro: 12345
# não
#
# Digite um número inteiro: 1011
# sim
#
#   Como enviar
#   Quando você estiver pronto para enviar, você pode fazer upload dos arquivos para cada parte da 
# tarefa na guia "Meu envio".
#
num = int(input('Digite um número inteiro: '))
adjacente = False
ultNum = 10 

while(num>0 and not adjacente):
    print("*")
    if(ultNum == num%10):
        adjacente = True
    else:
        ultNum = num%10

    num = num//10

if(adjacente):
    print('sim')
else:
    print('não')
