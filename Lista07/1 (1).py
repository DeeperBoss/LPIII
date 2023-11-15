class Contato:
  total_contatos = 0

  def __init__(self, nome, telefone):
      self.nome = nome
      self.telefone = telefone
      Contato.total_contatos += 1

  @classmethod
  def mostrar_total(cls):
      print(f"Total de contatos: {cls.total_contatos}")