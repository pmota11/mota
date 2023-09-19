def soma(a, b):
    print(a + b)

soma(9,10)

def ehpar(x):
    return x % 2 == 0

print(ehpar(2))
print(ehpar(3))

def par_ou_impar(x):
    if ehpar(x):
        return "par"
    else:
        return "impar"

print(par_ou_impar(2))
print(par_ou_impar(3))

def valida_int(numero, minimo, maximo):
    return numero >= minimo and numero <= maximo
    return minimo < numero < maximo
print(valida_int(5,5,10))
print(valida_int(1,5,10))


def barra():
    return "*" * 40

print(barra())
