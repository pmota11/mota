while True:
    try:
        num = int(input("entre com um número inteiro"))
        if num == 0:
            break
    except Exception:
        print("número invalido")

import random
for i in range(10):
    print(random.randint(1,10))

#outro ex
from random import randint

num_sort = random.randint(1,5)
num_escolha = int(input("entre com um numero inteiro"
                        ">= 1 e <=5: "))
if num_escolha == num_sort:
    print("voce acertou")
else:
    print("você errou")

#aleatorizar
from random import choice

frutas = ["uva","pera","maça","laranja"]
print(choice(frutas))
