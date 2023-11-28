class Livro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.disponivel = True

    def emprestar_livro(self):
       if self.disponivel:
        self.disponivel = False
        return f'O livro "{self.titulo}" foi emprestado.'
       else:
          return f'O livro "{self.titulo}" não está disponivel no momento.'
       
    def devolver_livro(self):
       if not self.disponivel:
          self.disponivel = True
          return f'O livro "{self.titulo}" já está disponivel.'
    
    def verificador_disponibilidade(self):
       return f'O livro "{self.titulo}" está disponivel.' if self.disponivel else f'O livro "{self.titulo}" não está disponivel.'
    