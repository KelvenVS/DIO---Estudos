from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
        pass
    
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("TV ligada !!!")
        
    def desligar(self):
        print("Desligando a TV")
        print("TV desligado !!!")
    #Remover um dos metodos , vai gera um erro no CMD
    
    def marca(self):
        return "Xiaomi"
    
controle = ControleTV()

controle.ligar()