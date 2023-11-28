class Aluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0
        def verificar_situacao(self):
            media = self.calcular_media()
            if media >= 6.0:
                return f'O aluno {self.nome} está aprovado com a media {media:.2f}'
            else:
                return f'O aluno {self.nome} está reprovado com a media {media:.2f}'