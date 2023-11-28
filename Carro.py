Carro:
    def __init__(self, modelo, marca, velocidade_atual=0):
        self.nome = modelo
        self.nome = marca
        self.velocidade_atual = velocidade_atual

    def acelarar(self, velocidade):
        self.velocidade_atual += velocidade
        return f'O carro acelerou para {self.velocidade_atual} km/h'
    def frear(self, velocidade):
        if self.velocidade_atual >= velocidade:
           self.velocidade_atual -= velocidade
           return f'O carro freou para {self.velocidade_atual} km/h.'
        else:
            self.velocidade_atual = 0
            return 'O carro parou a frenagem total.'
    def exibir_velocidade_atual(self):
        return f'A velocidade atual do carro é {self.velocidade_atual} km/h'
