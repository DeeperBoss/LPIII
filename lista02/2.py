import random


def lancar_dados():
  dado1 = random.randint(1, 6)
  dado2 = random.randint(1, 6)
  return dado1, dado2


def jogar_craps():
  dado1, dado2 = lancar_dados()
  soma = dado1 + dado2
  print(f"Dado 1: {dado1}, Dado 2: {dado2}")
  print(f"Ponto: {soma}")

  if soma in [7, 11]:
    print("Vc ganhou :-)")
    return
  elif soma in [2, 3, 12]:
    print("Vc perdeu :-(")
    return

  print("Iniciando estágio 2")
  ponto = soma
  jogada = 0

  while True:
    jogada += 1
    dado1, dado2 = lancar_dados()
    soma = dado1 + dado2
    print(f"Dado 1: {dado1}, Dado 2: {dado2}")
    print(f"Jogada {jogada}: {soma}")

    if soma == ponto:
      print("Vc ganhou :-)")
      return
    elif soma == 7:
      print("Vc perdeu :-(")
      return


jogar_craps()
