def primo(num):
    cont = 0
    div = num
    primo = True
    while div>0 and primo:
        if(num%div == 0):
            cont+=1
        div -=1
        if(cont == 3):
            primo = False
    
    if(cont<2):
        primo = False
    
    return primo

def n_primos(num:int):
    cont = 0
    while num > 0:
        if(primo(num)):
            cont+=1
        num -=1
    
    return cont
