class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    def calcular_salario_liquido(self):
        # Considerando desconto de 10% para impostos e beneficios.
        desconto = 0.1 * self.salario
        salario_liquido = self.salario - desconto
        return salario_liquido
    def exibir_informacoes(self):
        salario_liquido = self.calcular_salario_liquido()
        return f'Funcionario: {self.nome}, Salario: {self.salario}, Cargo: {self.cargo}'
    
