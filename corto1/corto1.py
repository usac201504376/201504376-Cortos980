N = 0
def Secuencia(N):
    for numero in range(2,376):
        while numero > 1:
            if numero%2 == 0:
                num = [numero/2]
                collatz = [] + num
            else:
                num2 = [3*numero + 1]
                collatz = [] + num2
                print (collatz)
    
    return N

Secuencia(N)