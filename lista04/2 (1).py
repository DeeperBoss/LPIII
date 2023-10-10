import datetime

class Contato:
    def __init__(self, nome, email, telefone, dataNascimento):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.dataNascimento = dataNascimento

    def setNome(self, nome):
        self.nome = nome

    def setEmail(self, email):
        self.email = email

    def setTelefone(self, telefone):
        self.telefone = telefone

    def setDataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email

    def getTelefone(self):
        return self.telefone

    def getDataNascimento(self):
        return self.dataNascimento

    def imprimirContato(self):
        print("Nome:", self.nome)
        print("Email:", self.email)
        print("Telefone:", self.telefone)
        print("Data de Nascimento:", self.dataNascimento)

    def calcularIdade(self):
        dataAtual = datetime.date.today()
        dataNascimento = datetime.datetime.strptime(self.dataNascimento, '%d/%m/%Y').date()
        idade = dataAtual.year - dataNascimento.year - ((dataAtual.month, dataAtual.day) < (dataNascimento.month, dataNascimento.day))
        return idade
