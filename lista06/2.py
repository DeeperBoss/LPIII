from datetime import datetime


class Data:

  def __init__(self, dia=1, mes=1, ano=1970):
    self.data = datetime(ano, mes, dia)

  def howManyDays(self, *args):
    if len(args) == 1:
      if isinstance(args[0], Data):
        outra_data = args[0].data
      else:
        raise TypeError("Argumento inválido")
    elif len(args) == 3:
      outra_data = datetime(args[2], args[1], args[0])
    else:
      raise TypeError("Número inválido de argumentos")

    return (self.data - outra_data).days

  def __str__(self):
    return self.data.strftime("%d/%m/%Y")
