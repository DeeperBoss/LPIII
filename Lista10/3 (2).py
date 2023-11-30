    class Pessoa:
      def __init__(self, nome, id, nascimento):
          self.nome = nome
          self.id = id
          self.nascimento = nascimento

      def __str__(self):
          return f'Nome: {self.nome}, ID: {self.id}, Nascimento: {self.nascimento}'

    class Politico(Pessoa):
      def __init__(self, nome, id, nascimento, siglaPartido, numeroPartido):
          super().__init__(nome, id, nascimento)
          self.siglaPartido = siglaPartido
          self.numeroPartido = numeroPartido

      def __str__(self):
          return super().__str__() + f', Sigla do Partido: {self.siglaPartido}, Número do Partido: {self.numeroPartido}'

    class Prefeito(Politico):
      def __init__(self, nome, id, nascimento, siglaPartido, numeroPartido, cidade):
          super().__init__(nome, id, nascimento, siglaPartido, numeroPartido)
          self.cidade = cidade

      def __str__(self):
          return super().__str__() + f', Cidade: {self.cidade}'

    class Governador(Politico):
      def __init__(self, nome, id, nascimento, siglaPartido, numeroPartido, estado):
          super().__init__(nome, id, nascimento, siglaPartido, numeroPartido)
          self.estado = estado

      def __str__(self):
          return super().__str__() + f', Estado: {self.estado}'

    # Programa de exemplo
    politicos = [
      Politico('João', 123, '01/01/2000', 'PT', 13),
      Prefeito('Maria', 456, '02/02/2000', 'PSDB', 45, 'São Paulo'),
      Governador('Carlos', 789, '03/03/2000', 'MDB', 15, 'Rio de Janeiro')
    ]

    for politico in politicos:
      print(politico)