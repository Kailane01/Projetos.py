class circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio**2
    
    def calcular_perimetro(self):
        return 2 * 3.14 * self.raio