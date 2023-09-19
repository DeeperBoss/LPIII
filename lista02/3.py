import numpy as np


def criar_tabuleiro():
  return np.full((5, 5), '-')


def adicionar_navios(tabuleiro, coordenadas):
  for coord in coordenadas:
    tabuleiro[coord] = '@'
  return tabuleiro


def atirar(tabuleiro, coord):
  if tabuleiro[coord] == '@':
    tabuleiro[coord] = 'X'
    return True
  else:
    tabuleiro[coord] = 'O'
    return False


def jogo():
  print("Welcome to Battleship!!!")

  # Criação dos tabuleiros
  tabuleiro1 = criar_tabuleiro()
  tabuleiro2 = criar_tabuleiro()

  # Adição dos navios
  coordenadas1 = [(0, 1), (1, 3), (2, 1), (3, 0), (3, 4)]
  coordenadas2 = [(0, 1), (0, 4), (2, 0), (3, 1), (4, 4)]

  tabuleiro1 = adicionar_navios(tabuleiro1, coordenadas1)
  tabuleiro2 = adicionar_navios(tabuleiro2, coordenadas2)

  # Jogo
  while '@' in tabuleiro1 and '@' in tabuleiro2:
    # Jogador 1
    coord = input("Jogador 1, insira as coordenadas para atirar: ")
    acertou = atirar(tabuleiro2, coord)
    if acertou:
      print("Jogador 1 acertou!")
    else:
      print("Jogador 1 errou!")

    # Jogador 2
    coord = input("Jogador 2, insira as coordenadas para atirar: ")
    acertou = atirar(tabuleiro1, coord)
    if acertou:
      print("Jogador 2 acertou!")
    else:
      print("Jogador 2 errou!")

  # Verificar quem ganhou
  if '@' not in tabuleiro1:
    print("Jogador 2 venceu!")
  else:
    print("Jogador 1 venceu!")


jogo()
