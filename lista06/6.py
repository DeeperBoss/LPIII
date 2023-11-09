              class RoboSimples:
                direcoes_validas = ['N', 'S', 'E', 'O', 'NE', 'NO', 'SE', 'SO']

                def __init__(self, nome, direcao):
                    if not nome or direcao not in self.direcoes_validas:
                        raise ValueError("Nome inválido ou direção inválida")
                    self.nome = nome
                    self.direcao = direcao

                def validaRobo(self):
                    return self.nome is not None and self.direcao in self.direcoes_validas

                def move(self, direcao):
                    if direcao not in self.direcoes_validas:
                        raise ValueError("Direção inválida")
                    self.direcao = direcao

                def __str__(self):
                    return f"({self.nome}, {self.direcao})"