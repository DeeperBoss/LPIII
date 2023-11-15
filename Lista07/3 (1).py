          from datetime import datetime, timedelta

          class Data:
              def __init__(self, dia, mes, ano):
                  self.dia = dia
                  self.mes = mes
                  self.ano = ano
                  self.data = datetime(self.ano, self.mes, self.dia)

              @staticmethod
              def howManyDaysUntilEndYear(d):
                  end_year = datetime(d.ano, 12, 31)
                  return (end_year - d.data).days

              @staticmethod
              def howManyDaysUntilNextMonth(d):
                  if d.mes == 12:
                      next_month = datetime(d.ano + 1, 1, 1)
                  else:
                      next_month = datetime(d.ano, d.mes + 1, 1)
                  return (next_month - d.data).days

              @staticmethod
              def isBisexto(d):
                  return d.ano % 4 == 0 and (d.ano % 100 != 0 or d.ano % 400 == 0)

              @staticmethod
              def dayOfWeek(d):
                  days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
                  return days[d.data.weekday()]

              @staticmethod
              def dayToPrintShort(d):
                  return d.data.strftime("%d/%m/%Y")

              @staticmethod
              def dayToPrintLong(d):
                  months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
                  return f"{d.dia} de {months[d.mes - 1]} de {d.ano}"