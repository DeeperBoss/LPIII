# Criando objetos das classes Data, Hora e Contato
data = Data(2022, 12, 31)
hora = Hora(14, 30)
contato = Contato('João', 'joao@example.com', '999999999')

# Criando um agendamento
agendamento = Agendamento(data, hora, contato)

# Imprimindo o agendamento
print(agendamento.imprimeAgendamento())