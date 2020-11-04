# Exercício 1 - FizzBuzz
# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve
# 
# 'Fizz' se o número for divisível por 3 e não for divisível por 5;
# 
# 'Buzz' se o número for divisível por 5 e não for divisível por 3;
# 
# 'FizzBuzz' se o número for divisível por 3 e por 5;
# 
# Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.
# 
# Exemplos de execução no Python Shell
# >>>fizzbuzz(3)
# "Fizz"
# >>>fizzbuzz(5)
# "Buzz"
# >>>fizzbuzz(15)
# "FizzBuzz"
# >>>fizzbuzz(4)
# 4
#

def fizzbuzz(num:int):
    numDiv3 = False
    numDiv5 = False

    if(num%3==0):
        numDiv3 = True

    if (num%5==0):
        numDiv5 = True

    if(numDiv3 and not numDiv5):
        return "Fizz"
    elif(not numDiv3 and numDiv5):
        return "Buzz"
    elif(numDiv3 and numDiv5):
        return "FizzBuzz"
    elif not(numDiv3 and numDiv5):
        return num
        