class Data:

  def __init__(self, dia, mes, ano):
    self.dia = dia
    self.mes = mes
    self.ano = ano

  def isPrevious(self, outraData):
    if self.ano < outraData.ano:
      return True
    elif self.ano == outraData.ano and self.mes < outraData.mes:
      return True
    elif self.ano == outraData.ano and self.mes == outraData.mes and self.dia < outraData.dia:
      return True
    else:
      return False

  def howManyDays(self, outraData):
    if self.isPrevious(outraData):
      return -self.howManyDays(self)
    else:
      days = 0
      while self.isPrevious(outraData):
        days -= 1
        self.addDays(1)
      return days

  def addDays(self, days):
    while days > 0:
      daysInMonth = self.daysInMonth()
      if self.dia + days <= daysInMonth:
        self.dia += days
        days = 0
      else:
        days -= daysInMonth - self.dia + 1
        self.dia = 1
        self.addMonths(1)

  def addMonths(self, months):
    while months > 0:
      if self.mes == 12:
        self.mes = 1
        self.ano += 1
      else:
        self.mes += 1
      months -= 1

  def daysInMonth(self):
    if self.mes == 2:
      if self.isLeapYear():
        return 29
      else:
        return 28
    elif self.mes in [4, 6, 9, 11]:
      return 30
    else:
      return 31

  def isLeapYear(self):
    if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
      return True
    else:
      return False
