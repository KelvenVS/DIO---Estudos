class Pessoa:
    def __init__(self, nome=None , idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_pessoa_pela_data_nasc(self, ano=None, mes=None, dia=None, nome=None):
        idade = 2025 - ano
        return Pessoa(nome, idade)
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'
    
    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18
        
p1 = Pessoa('Kelven',24)
print(p1)

p2 = Pessoa.criar_pessoa_pela_data_nasc(2000, 6, 21, "Kelven")
print(p2)

print(Pessoa.e_maior_de_idade(p1.idade))
print(Pessoa.e_maior_de_idade(18))