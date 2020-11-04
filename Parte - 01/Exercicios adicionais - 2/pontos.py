#   Exercício 1 - Distância entre dois pontos
#   Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, 
# às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, 
# às coordenadas x e y de um outro ponto no mesmo plano.
#   
#   Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
#   
#   longe
#   
#   na saída. Caso o contrário, quando a distância for menor que 10, imprima
#   
#   perto
#   
#   Dica: lembre-se que a fórmula da distância para dois pontos num plano cartesiano é a seguinte:
#
#   d(x, y) = sqrt((x_1 - x_2)^2 + (y_1 - y_2)^2)

import math

x1 = float(input("Digite o valor de X1 "))
y1 = float(input("Digite o valor de Y1 "))
x2 = float(input("Digite o valor de X2 "))
y2 = float(input("Digite o valor de Y2 "))

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if(dist > 10 ):
    print("longe")
else:
    print ("perto")