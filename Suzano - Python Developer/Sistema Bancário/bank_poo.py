from datetime import date

class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido")
        else:
            self._cpf = cpf
        self._nome: str = nome
        self._data_nascimento: date = data_nascimento
    
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        return cpf.isdigit() and len(cpf) == 11
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, novo_cpf: str):
        if self.validar_cpf(novo_cpf):
            self._cpf = novo_cpf
        else:
            raise ValueError("CPF inválido")
    
    def class_name(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave.capitalize()}:{valor}' for chave,valor in self.__dict__.items()])}"

pessoa = PessoaFisica(cpf="1234567890", nome="João Silva", data_nascimento=date(1990, 5, 10))
print(pessoa)
pessoa.cpf = "48656250892"