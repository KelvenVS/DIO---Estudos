import random
from abc import ABC, abstractmethod
from datetime import date, datetime

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
    def __init__(self, pessoa, endereco: str):
        self._pessoa = pessoa
        self._endereco: str = endereco
        self._contas: list = []
    
    def adicionar_conta(self, conta):
        """Adiciona uma conta ao cliente."""
        if isinstance(conta, Conta):
            self._contas.append(conta)
            print("Conta adicionada com sucesso!")
        else:
            print("Erro: objeto inválido.")
    
    @classmethod
    def criar_cliente(cls):
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

        # Criar instância de PessoaFisica e Cliente
        pessoa = PessoaFisica(cpf, nome, data_nascimento)
        cliente = cls(pessoa, endereco)
        
        resposta = input("Deseja criar uma conta agora? (S/N): ").strip().lower()
        if resposta == 's':
            cliente.adicionar_conta(ContaCorrente.insert_conta())

        return cliente
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave.capitalize()}:{valor}' for chave,valor in self.__dict__.items()])}"

class Conta(ABC):
    def __init__(self, saldo: float, numero: str, agencia: str):
        self._saldo: float = saldo
        self._numero: str = numero
        self._agencia: str = agencia
        self._extrato: list = []
    
    @property
    def saldo(self):
        return self._saldo
    
    @staticmethod
    def gerar_numero_conta():
        return f"{random.randint(1, 10):06d}"
    
    @abstractmethod
    def insert_conta(self):
        pass
            
    @abstractmethod
    def realizar_transacao(self, transacao, valor: float):
        pass

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta, valor: float):
        pass
        
class Saque(Transacao):
    def registrar(self, conta, valor: float):
        if conta.saldo >= valor:
            saldo_anterior = conta.saldo
            conta._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            
            conta._extrato.append(
                Extrato(operacao = self.__class__.__name__,
                                    data_hora = datetime.now(),
                                    saldo_anterior = saldo_anterior,
                                    valor = valor,
                                    saldo_atual= conta._saldo
                    )
                )
        else:
            print("Saldo insuficiente para saque.")
            
class Deposito(Transacao):
    def registrar(self, conta, valor: float):
        if valor > 0:
            saldo_anterior = conta._saldo
            conta._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
          
            conta._extrato.append(
                Extrato(operacao = self.__class__.__name__,
                                    data_hora = datetime.now(),
                                    saldo_anterior = saldo_anterior,
                                    valor = valor,
                                    saldo_atual= conta._saldo
                    )
                )
        else:
            print("Valor inválido para depósito.")

class Extrato:
    def __init__(self, operacao: str, data_hora: datetime, saldo_anterior: str, valor: str, saldo_atual: str):
        self._operacao: str = operacao
        self._data_hora: datetime = data_hora
        self._saldo_anterior: str = saldo_anterior
        self._valor: str = valor
        self._saldo_atual: str = saldo_atual
        
    def __str__(self):
        return f'Operação: {self._operacao} | Data e Hora: {self._data_hora} | Saldo Anterior: {self._saldo_anterior} | Saldo Atual: {self._saldo_atual}'
            
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, transacoes_dia = 5, limite_saque = 500):
        super().__init__(saldo, numero, agencia)
        self._transacoes_dia = transacoes_dia
        self._limite_saque = limite_saque
        self._extrato = []
    
    @classmethod   
    def insert_conta(cls):
        saldo = 500
        numero = cls.gerar_numero_conta()
        agencia = '0001'
        extrato = []
        return cls(saldo, numero, agencia, extrato)
    
    def realizar_transacao(self, transacao: Transacao, valor: float):
        if isinstance(transacao, Saque) and valor > self._limite_saque:
            print(f"Saque excede o limite de R${self._limite_saque:.2f}.")
        else:
            transacao.registrar(self, valor)
    
    def exibir_extrato(self):
        if not self._extrato:
            print("Nenhuma transação foi realizada.")
        else:
            print("\n=== Extrato ===")
            for transacao in self._extrato:
                print(transacao)
            print("================")
    
    def __str__(self):
        return f"Tipo: {self.__class__.__name__} | Agência: {self._agencia} | Numero: {self._numero:>5} | Saldo: {self._saldo:>5}"

if __name__ == '__main__':
    cliente1 = Cliente.criar_cliente()
    cliente1.adicionar_conta(ContaCorrente.insert_conta())

    for conta in cliente1._contas:
        print(conta)

    conta_corrente = cliente1._contas[0]
    conta_corrente.realizar_transacao(Deposito(), 2000)  # Depósito
    conta_corrente.realizar_transacao(Saque(), 400)    # Saque

    for conta in cliente1._contas:
        conta.exibir_extrato()