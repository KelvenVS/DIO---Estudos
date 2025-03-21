from datetime import date

class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        self._cpf: str = cpf
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

class Cliente(PessoaFisica):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str, contas: list):
        super().__init__(cpf, nome, data_nascimento)
        self._endereco: str = endereco
        self._contas: list = contas
    
    @classmethod
    def insert_cliente(cls):
        while True:
            cpf = input("Digite o CPF: ")
            if cls.validar_cpf(cpf):
                break
            print("CPF inválido! Digite um CPF com 11 dígitos numéricos.")
            
        nome = input("Digite o nome: ")
        data_nascimento = date.fromisoformat(input("Digite a data de nascimento (YYYY-MM-DD): "))
        endereco = input("Digite o endereço: ")
        contas = []
        return cls(cpf, nome, data_nascimento, endereco, contas)
    

pessoa = PessoaFisica(cpf="12345678900", nome="João Silva", data_nascimento=date(1990, 5, 10))
print(pessoa)
pessoa.cpf = "48656250892"

cliente = Cliente.insert_cliente()
print(cliente)