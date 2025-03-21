import random
from datetime import date

class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        self._cpf: str = cpf
        self._nome: str = nome
        self._data_nascimento: date = data_nascimento
    
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        return cpf.isdigit() and len(cpf) == 11
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave.capitalize()}:{valor}' for chave,valor in self.__dict__.items()])}"

class Cliente:
    def __init__(self, pessoa, endereco: str, contas: list):
        self._pessoa = pessoa
        self._endereco: str = endereco
        self._contas: list = contas
    
    @classmethod
    def insert_cliente(cls):
        print("Insira os dados do cliente:\n")

        # Coletar e validar CPF
        while True:
            cpf = input("Digite o CPF: ")
            if PessoaFisica.validar_cpf(cpf):
                break
            print("CPF inválido! Digite um CPF com 11 dígitos numéricos.")
        
        # Coletar nome
        nome = input("Digite o nome: ")
        
        # Coletar data de nascimento
        while True:
            try:
                data_nascimento = date.fromisoformat(input("Digite a data de nascimento (YYYY-MM-DD): "))
                break
            except ValueError:
                print("Data inválida! Por favor, use o formato YYYY-MM-DD.")
        
        # Coletar endereço
        endereco = input("Digite o endereço: ")

        # Criar instância de PessoaFisica
        pessoa = PessoaFisica(cpf, nome, data_nascimento)
        
        contas = [Conta.insert_conta()]

        # Criar e retornar instância de Cliente
        return cls(pessoa, endereco,contas)
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave.capitalize()}:{valor}' for chave,valor in self.__dict__.items()])}"
    
class Historico:
    pass

class Conta:
    def __init__(self, saldo: float, numero: str, agencia: str, historico: Historico):
        self._saldo: float = saldo
        self._numero: str = numero
        self._agencia: str = agencia
        self._historico: Historico = historico
    
    @staticmethod
    def gerar_numero_conta():
        return f"{random.randint(1, 10):06d}"
    
    @classmethod
    def insert_conta(cls,  tipo="Corrente"):
            if tipo == "Corrente":
                saldo = 0.0
                numero = cls.gerar_numero_conta()
                agencia = '0001'
                historico = Historico()
                return ContaCorrente(saldo, numero, agencia, historico)

class ContaCorrente(Conta):
    def __init__(self,saldo, numero, agencia, historico, transacoes_dia = 5, limite_saque = 500):
        super().__init__(saldo, numero, agencia, historico)
        self._transacoes_dia = transacoes_dia
        self._limite_saque = limite_saque
    
    def __str__(self):
        return f"Tipo: {self.__class__.__name__} | Agência: {self._agencia} | Numero: {self._numero:>5} | Saldo: {self._saldo:>5}"

cliente1 = Cliente.insert_cliente()
cliente1._contas.append(Conta.insert_conta("Corrente"))

for conta in cliente1._contas:
    print(conta)