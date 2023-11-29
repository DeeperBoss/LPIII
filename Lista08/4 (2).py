class SegmentoReta:
  def __init__(self, P1, P2):
      self.P1 = P1
      self.P2 = P2
      self.dimensao = self.calculaDimensao()

  def imprimeSegmentoReta(self):
      return f'O segmento de reta inicia no ponto ({self.P1.x}, {self.P1.y}) e finaliza no ponto ({self.P2.x}, {self.P2.y}) com dimensão {self.dimensao}.'

  def calculaDimensao(self):
      return Ponto2DUtils.distance(self.P1, self.P2)