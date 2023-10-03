# operação para verificar se uma data é válida
def dataÉVálida(umDia, umMês, umAno):
  maxDia = 0

  # verifica se o mês é fevereiro e se o ano é bissexto
  if umMês == 2:
    if (umAno % 4 == 0 and umAno % 100 != 0) or umAno % 400 == 0:
      maxDia = 29
    else:
      maxDia = 28
  elif umMês == 4 or umMês == 6 or umMês == 9 or umMês == 11:
    maxDia = 30
  else:
    maxDia = 31

  # verifica se o dia é válido
  if umDia >= 1 and umDia <= maxDia:
    return True
  else:
    return False


# operação para retornar o dia da semana para uma data válida
def diaDaSemana(umDia, umMês, umAno):
  q = umDia
  m = umMês
  K = umAno % 100
  J = umAno // 100
  h = (q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7

  # retorna o dia da semana correspondente
  if h == 0:
    return "sábado"
  elif h == 1:
    return "domingo"
  elif h == 2:
    return "segunda-feira"
  elif h == 3:
    return "terça-feira"
  elif h == 4:
    return "quarta-feira"
  elif h == 5:
    return "quinta-feira"
  elif h == 6:
    return "sexta-feira"
  else:
    return "dia inválido"


# operação para inicializar uma data
def inicializaData(umDia, umMês, umAno):
  dia = 0
  mês = 0
  ano = 0

  # verifica se a data é válida
  if dataÉVálida(umDia, umMês, umAno):
    dia = umDia
    mês = umMês
    ano = umAno

    # obtém o dia da semana correspondente
    diaSemana = diaDaSemana(dia, mês, ano)

    # imprime a data inicializada e o dia da semana correspondente
    print("Data inicializada: {}/{}/{} ({})".format(dia, mês, ano, diaSemana))
  else:
    print("Data inválida: {}/{}/{}".format(umDia, umMês, umAno))


# função principal
def main():
  # inicializa a data 31/02/2000
  inicializaData(31, 2, 2000)

  # inicializa a data 29/02/2000
  inicializaData(29, 2, 2000)

  # inicializa a data 29/02/1900
  inicializaData(29, 2, 1900)

  # inicializa a data 31/04/2000
  inicializaData(31, 4, 2000)

  # inicializa a data 31/06/2000
  inicializaData(31, 6, 2000)

  # inicializa a data 31/09/2000
  inicializaData(31, 9, 2000)

  # inicializa a data 31/11/2000
  inicializaData(31, 11, 2000)


if __name__ == "__main__":
  main()
