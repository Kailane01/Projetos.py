class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_consultas =[]

    def adicionar_consulta(self, consulta):
        self.historico_consultas.append(consulta)
        return f'Consultas adicionadas ao historico para o paciente {self.nome}.'
    
    def exibir_consultas_realizadas(self):
        if not self.historico_consulta:
            return 'Nenhuma consulta registrada.'
        else:
            return f'Consultas realizdas pelo paciente {self.nome}:\n{", ".join(self.historico_consultas)}'
        