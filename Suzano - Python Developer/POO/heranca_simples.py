class Veiculo:
    def __init__(self, marca, rodas, placa, num_pass, valor):
        self.placa = placa
        self.marca = marca
        self.rodas = rodas
        self.num_pass = num_pass
        self.valor = valor

    def movimentar_para_frente(self):
        print("Andando para frente.")

    def movimentar_para_tras(self):
        print("Andando para trás.")

    def virar_a_direita(self):
        print("Virando à direita.")

    def virar_a_esquerda(self):
        print("Virando à esquerda.")

    def ligar_motor(self):
        print("Ligando o motor.")

    def __str__(self):
        return f"Placa: {self.placa} | Marca: {self.marca} | Rodas: {self.rodas} | Número de Passageiros: {self.num_pass} | Valor: {self.valor}"


class Motocicleta(Veiculo):
    def __init__(self, marca, placa, num_pass, valor, rodas=2):
        super().__init__(marca, rodas, placa, num_pass, valor)


class Caminhao(Veiculo):
    def __init__(self, marca, placa, num_pass, valor, carregado=False, rodas=6):
        super().__init__(marca, rodas, placa, num_pass, valor)
        self.carregado = carregado

    def esta_carregado(self):
        return "Está carregado." if self.carregado else "Não está carregado."


moto1 = Motocicleta("Yamaha", "ABC-1234", 3, 20000.00)
print(moto1)

caminhao1 = Caminhao("Scania", "ABC-4321", 3, 150000.00, True)
print(caminhao1)

print(caminhao1.esta_carregado())
caminhao1.ligar_motor()
caminhao1.movimentar_para_frente()
caminhao1.movimentar_para_frente()
caminhao1.virar_a_direita()
caminhao1.virar_a_direita()
