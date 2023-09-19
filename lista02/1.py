import math

# Leituras do multímetro
leituras = [10, 12, 10, 11, 12, 11, 10, 12, 11, 10]

# Cálculo da média
media = sum(leituras) / len(leituras)

# Cálculo do desvio padrão
desvio_padrao = math.sqrt(sum((x - media) ** 2 for x in leituras) / len(leituras))

# Verificar se o multímetro está operacional
if desvio_padrao > 0.1 * media:
    estado = "O multímetro não está operacional"
else:
    estado = "O multímetro está operacional"

print("Leituras: ", leituras)
print("Média: ", media)
print("Desvio padrão: ", desvio_padrao)
print(estado)
