matriz = []
for i in range(3):
    linha = []
    for j in range(4):
        produto = int(input(f"número de produtos por período: {i+1} {j+1}"))
        linha.append(produto)
    matriz.append(linha)
    if produto < 0:
        int(input("Digite novamente:"))

print("matriz:")
for linha in matriz:
    print(linha)

c = sum(matriz[0])
c1 = sum(matriz[1])
b = sum(matriz[2])
print("número total de vendas de camisetas:",{c})
print("número de canecas vendidas:", {c1})
print("número de bonés vendidos:", {b})



