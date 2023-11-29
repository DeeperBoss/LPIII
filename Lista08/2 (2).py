            class DataHora:
              def __init__(self, data, hora):
                  self.data = data
                  self.hora = hora

              def toString(self):
                  return f'Data: {self.data.toString()}, Hora: {self.hora.toString()}'

              def isEqual(self, outroObjeto):
                  return self.data.isEqual(outroObjeto.data) and self.hora.isEqual(outroObjeto.hora)

              def isGreather(self, outroObjeto):
                  if self.data.isGreather(outroObjeto.data):
                      return True
                  elif self.data.isEqual(outroObjeto.data):
                      return self.hora.isGreather(outroObjeto.hora)
                  else:
                      return False

              def isLower(self, outroObjeto):
                  if self.data.isLower(outroObjeto.data):
                      return True
                  elif self.data.isEqual(outroObjeto.data):
                      return self.hora.isLower(outroObjeto.hora)
                  else:
                      return False