class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def verificar_triangulo_valido(self):
        return (self.lado1 + self.lado2 > self.lado3) and (self.lado1 + self.lado3 > self.lado2) and (self.lado2 + self.lado3 > self.lado1)
    def calcular_area(self):
       if self.verificar_triangulo_valido(): 
    # Fórmula de Heron para calcular a área de um triângulo 
        s = (self.lado1 + self.lado2 + self.lado3) / 2 
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5 
        return area
       else:
          return "Triangulo invalido. Não é possivel calcular a area."