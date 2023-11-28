class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    def calcular_parimetro(self):
        return 2 * (self.largura + self.altura)