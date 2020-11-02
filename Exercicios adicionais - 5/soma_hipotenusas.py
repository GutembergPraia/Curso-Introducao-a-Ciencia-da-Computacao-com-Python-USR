def é_hipotenusa(num:int):
    i = 0
    j= 0
    hipotenusa = False
    while (i < num and not hipotenusa):
        while j < num:
            if(pow(num,2)==pow(i,2)+pow(j,2)):
                hipotenusa = True
            j+=1
        i+=1
        j = 0
    return hipotenusa

def soma_hipotenusas(num:int):
    i = 1
    soma = 0
    while (i<=num):
        if(é_hipotenusa(i)):
            soma += i
        i+=1
    return soma