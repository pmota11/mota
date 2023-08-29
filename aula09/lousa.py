frase = "hello world!"

print(frase)
print(len(frase))
print(frase[0])
print(frase[1])

a = "Hello"
b = "World"
c = " "
d = "!"

print(a+c+b+d)
print(a+" " + b + d *3)
print(a + " " +b + "!")

print(frase[0:5])
print(frase[6:12])

frase_lista = list(frase)
print(frase_lista)
frase_lista[5]=","
print(frase_lista)

frase_inteira = " ".join(frase_lista)
print(frase_inteira )

print()
