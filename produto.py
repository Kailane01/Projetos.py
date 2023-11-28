class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def calcular_valor_total_em_estoque(self):
        return self.preco * self.quantidade_em_estoque
    
    def verificar_disponibilidade(self, quantidade_desejada):
        return self.quantidade_em_estoque >= quantidade_desejada