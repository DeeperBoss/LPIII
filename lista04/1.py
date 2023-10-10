class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def inicializarData(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def verificarData(self):
        if self.dia < 1 or self.dia > 31:
            return False
        if self.mes < 1 or self.mes > 12:
            return False
        if self.ano < 0:
            return False
        if self.mes == 2:
            if self.dia > 29:
                return False
            if self.dia == 29 and (self.ano % 4 != 0 or (self.ano % 100 == 0 and self.ano % 400 != 0)):
                return False     
        if self.mes in [4, 6, 9, 11] and self.dia > 30:
            return False
        return True
    
    def setDia(self, dia):
        self.dia = dia

    def setMes(self, mes):
        self.mes = mes

    def setAno(self, ano):
        self.ano = ano

    def getDia(self):
        return self.dia
    
    def getMes(self):
        return self.mes
    
    def getAno(self):
        return self.ano
    
    def imprimirData(self):
        return f"{self.dia:02}/{self.mes:02}/{self.ano}"
    
    def imprimirDataExtenso(self):
        meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        return f"{self.dia} de {meses[self.mes-1]} de {self.ano}"
    
    