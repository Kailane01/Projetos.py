class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f'Deposito de {valor} realizado. Novo saldo: {self.saldo}'
    
    def sacar(self, valor):
        if valor > self.saldo:
            return 'Saldo Insuficiente.'
        else:
            self.saldo -= valor
            return f'Saque de {valor} realizado. Novo saldo: {self.saldo}'