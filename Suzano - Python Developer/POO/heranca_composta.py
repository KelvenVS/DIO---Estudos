class Animal:
    def __init__(self, num_patas, peso, tamanho):
        self.num_patas = num_patas
        self.peso = peso
        self.tamanho = tamanho
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave.capitalize()}:{valor}' for chave,valor in self.__dict__.items()])}"

    def class_name(self):
        return self.__class__.__name__
    
class Mamifero(Animal):
    def __init__(self, num_patas, peso, tamanho):
        super().__init__(num_patas, peso, tamanho)
        
    def amamenta(self):
        return True

class Ave(Animal):
    def __init__(self, num_patas, peso, tamanho):
        super().__init__(num_patas, peso, tamanho)
        
    def voa(self):
        return True
    
    def bota_ovo(self):
        return True

class Cachorro(Mamifero):
    def __init__(self, nome, cor, num_patas, peso, tamanho):
        self.nome = nome
        self.cor = cor
        super().__init__(num_patas, peso, tamanho)

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornintorrinco(Ave, Mamifero):
    def __init__(self, nome, cor, num_patas, peso, tamanho):
        self.nome = nome
        self.cor = cor
        Ave.__init__(self, num_patas, peso, tamanho)
        Mamifero.__init__(self, num_patas, peso, tamanho)

    def voa(self):
        return False
        
if __name__ == "__main__":
    ## Herança Simples Cachorro
    dog1 = Cachorro("Ralf", "Preto e Bege", 4, 10, "25cm")
    print(dog1)
    print(f"{dog1.class_name()} amamenta" if dog1.amamenta() else "Não amamenta")

    ## Herança Composta Ornitorrinco
    orn1 = Ornintorrinco("Pedro", "Azul-Escuro", 4, 15, "30cm")
    print(orn1)
    print(f"{orn1.class_name()} amamenta os filhotes" if orn1.amamenta() else f"{orn1.class_name()} não amamenta os filhotes")
    print(f"{orn1.class_name()} voa" if orn1.voa() else f"{orn1.class_name()} não voa")
    print(f"{orn1.class_name()} bota ovos" if orn1.bota_ovo() else f"{orn1.class_name()} Não bota ovos")