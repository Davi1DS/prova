#exercício de vetores

vetor = []
c = []

for i in range(5):
    num = int(input(f"digite o número de chamados ({i+1}):"))
    c.append(num)
    quantidade = len(c)
    if num < 0:
        print()

print(f"o número de chamadas durante a semana é {sum(c)}:")
print(f"A média de chamadas por dia é {sum(c)/5}")
print(f"O dia com maior número de chamados é {c.index(max(c))}")

print("--------Relatório semanal----------")
print("dias da semana: segunda/terça/quarta/quinta/sexta")
print(f"nº de chamados {len(c)}")





