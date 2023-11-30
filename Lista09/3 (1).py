from datetime import datetime


class Livro:

  def __init__(self, titulo, autor, nroPaginas, anoPublicacao):
    self.titulo = titulo
    self.autor = autor
    self.nroPaginas = nroPaginas
    self.anoPublicacao = anoPublicacao

  def toString(self):
    return f'{self.titulo} por {self.autor}, {self.nroPaginas} páginas, publicado em {self.anoPublicacao}'

  def isOlder(self, other):
    return self.anoPublicacao < other.anoPublicacao


class LivroBiblioteca(Livro):

  def __init__(self, titulo, autor, nroPaginas, anoPublicacao):
    super().__init__(titulo, autor, nroPaginas, anoPublicacao)
    self.emprestado = False
    self.dataDevolucao = None

  def isAvailable(self):
    return not self.emprestado

  def borrow(self):
    if self.isAvailable():
      self.emprestado = True
      self.dataDevolucao = datetime.now()


class LivroLivraria(Livro):

  def __init__(self, titulo, autor, nroPaginas, anoPublicacao, preco, estoque):
    super().__init__(titulo, autor, nroPaginas, anoPublicacao)
    self.preco = preco
    self.estoque = estoque

  def sell(self):
    if self.estoque > 0:
      self.estoque -= 1
      return True
    return False

  def isAvailable(self):
    return self.estoque > 0


# Programa de exemplo
livro1 = Livro('Livro 1', 'Autor 1', 200, 1990)
livro2 = LivroBiblioteca('Livro 2', 'Autor 2', 300, 2000)
livro3 = LivroLivraria('Livro 3', 'Autor 3', 400, 2010, 50, 10)

print(livro1.toString())
print(livro2.toString())
print(livro3.toString())

print(livro1.isOlder(livro2))
print(livro2.isAvailable())
print(livro3.isAvailable())

livro2.borrow()
livro3.sell()

print(livro2.isAvailable())
print(livro3.isAvailable())
