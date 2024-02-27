#Writing a Module for factorial to be used later
def Fact(x):
    fact=1
    for i in range(x):
        fact=fact*(i+1)
    return int(fact)

def Permute(a,b):
    x=Fact(a)
    y=Fact(a-b)
    x=int(x/y)
    return int(x)

def Combine(n,r):
    comb=Permute(n,r)  #Using the previously defined function for Permutaions
    w=Fact(r)
    comb=comb/w
    return comb
    
