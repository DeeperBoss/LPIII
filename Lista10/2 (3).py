  class Pessoa:
    def __init__(self, nome, id, nascimento):
        self.nome = nome
        self.id = id
        self.nascimento = nascimento

    def CalculaEmprestimo(self):
        return 1000

  class Funcionario(Pessoa):
    def __init__(self, nome, id, nascimento, admissao, salario):
        super().__init__(nome, id, nascimento)
        self.admissao = admissao
        self.salario = salario

    def CalculaEmprestimo(self):
        return max(1000, self.salario * 0.75)

  class ChefeDeDepartamento(Funcionario):
    def __init__(self, nome, id, nascimento, admissao, salario, departamento, promocaoChefe):
        super().__init__(nome, id, nascimento, admissao, salario)
        self.departamento = departamento
        self.promocaoChefe = promocaoChefe

    def CalculaEmprestimo(self):
        return self.salario * 3

  pessoa = Pessoa('João', 123, '01/01/2000')
  funcionario = Funcionario('Maria', 456, '02/02/2000', '03/03/2020', 2000)
  chefe = ChefeDeDepartamento('Carlos', 789, '03/03/2000', '04/04/2020', 3000, 'Vendas', '05/05/2021')

  for p in [pessoa, funcionario, chefe]:
    print(p.CalculaEmprestimo())