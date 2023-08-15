
estoque = {"Camiseta Rosa":[10,50.0], "Camiseta Preta":[20,70.0], "Camiseta Branca":[20,70.0]}

venda = [["Camiseta Rosa",5],["Camiseta Preta", 10], ["Camiseta Branca",10]]

total = 0

for operação in venda:
    produto,quantidade = operação
    preco = estoque[produto][1]
    custo = preco*quantidade
    print(f"{produto}:{quantidade} X {preco} = {custo}")
    estoque[produto][0]-= quantidade
    total += custo

print(f"Custo total:{total}")

for chave, dados in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", dados[0])
    print(f"Preço: R${dados[1]}")

