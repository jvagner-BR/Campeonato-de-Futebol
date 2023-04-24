import random

# Definindo os times
times = ["boladosFc", "bençaFc", "soNaBrisaFc", "nadaConstaFc"]

# Criando dicionário de pontuação inicial
pontuacao = {time: 0 for time in times}
print(pontuacao)

# Loop para simular os jogos
for i, time1 in enumerate(times):
    for time2 in times[i + 1:]:
        # Gerando placar aleatório
        placar_time1 = random.randint(0, 5)
        placar_time2 = random.randint(0, 5)

        # Calculando pontos de acordo com o placar
        if placar_time1 > placar_time2:
            pontuacao[time1] += 3
        elif placar_time1 < placar_time2:
            pontuacao[time2] += 3
        else:
            pontuacao[time1] += 1
            pontuacao[time2] += 1

# Exibindo a pontuação final
print("Pontuação final:")
for time, pontos in pontuacao.items():
    print(f"{time}: {pontos} pontos")

    # Encontrando o ganhador
pontuacao_items = list(pontuacao.items())
pontuacao_items.sort(key=lambda x: x[1], reverse=True)
if pontuacao_items[0][1] != pontuacao_items[1][1]:
    print(f"O ganhador do campeonato é {pontuacao_items[0][0]}!")
else:
    print(f"Houve um empate entre os times vencedores!{pontuacao_items[0][0]} e {pontuacao_items[1][0]}")
