      class Contato:
        def __init__(self, nome, endereco, telefone, email):
            self.nome = nome
            self.endereco = endereco
            self.telefone = telefone
            self.email = email

      class PessoaFisica(Contato):
        def __init__(self, nome, cpf, endereco, data_aniversario, telefone, email):
            super().__init__(nome, endereco, telefone, email)
            self.cpf = cpf
            self.data_aniversario = data_aniversario

      class PessoaJuridica(Contato):
        def __init__(self, nome, cnpj, endereco, faturamento, telefone, email):
            super().__init__(nome, endereco, telefone, email)
            self.cnpj = cnpj
            self.faturamento = faturamento

      class Agenda:
        def __init__(self):
            self.contatos = []

        def adicionar_contato(self, contato):
            self.contatos.append(contato)

        def listar_contatos(self):
            for contato in self.contatos:
                print(contato.nome)

        def buscar_contato(self, cpf_cnpj):
            for contato in self.contatos:
                if isinstance(contato, PessoaFisica) and contato.cpf == cpf_cnpj:
                    return contato
                elif isinstance(contato, PessoaJuridica) and contato.cnpj == cpf_cnpj:
                    return contato
            return None

      # Programa de exemplo
      agenda = Agenda()
      agenda.adicionar_contato(PessoaFisica('João', '123', 'Rua 1', '01/01/2000', '1111-1111', 'joao@email.com'))
      agenda.adicionar_contato(PessoaJuridica('Empresa X', '456', 'Rua 2', 1000000, '2222-2222', 'empresa@email.com'))

      agenda.listar_contatos()

      contato = agenda.buscar_contato('123')
      if contato:
        print(contato.nome)