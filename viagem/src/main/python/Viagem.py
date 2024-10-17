# Viagem.py

class Viagem:
    def __init__(self, destino, data, custo):
        self.destino = destino
        self.data = data
        self.custo = custo

    def mostrar_valor(self):
        return self.custo

    def __repr__(self):
        return f"Viagem(destino='{self.destino}', data='{self.data}', custo={self.custo})"

# Agenda.py

from viagem.src.main.python.Viagem import Viagem

class Agenda:
    __viagens: Viagem = []

    def __init__(self):
        self.__viagens = []

    def createViagem(self, viagem):
        self.__viagens.append(viagem)

    def readViagens(self):
        return self.__viagens

    def updateViagem(self, index, updated_viagem):
        self.__viagens[index] = updated_viagem

    def deleteViagem(self, index):
        self.__viagens.pop(index)
        
    def clearViagens(self):
        self.__viagens = []

    def mostrar_valor_viagem(self, index):
        if 0 <= index < len(self.__viagens):
            return self.__viagens[index].mostrar_valor()
        else:
            return "Índice inválido."
