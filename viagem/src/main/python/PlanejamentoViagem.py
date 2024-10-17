# PlanejamentoViagem.py

class PlanejamentoViagem:
    def __init__(self, local: str, horario: str, data: str, nome_contratante: str, valor: float):
        self.__local = local
        self.__horario = horario
        self.__data = data
        self.__nome_contratante = nome_contratante
        self.__valor = valor

    def __repr__(self):
        return (f"PlanejamentoViagem(local={self.__local}, horario={self.__horario}, "
                f"data={self.__data}, nome_contratante={self.__nome_contratante}, "
                f"valor={self.__valor})")

    def mostrar_valor(self):
        return self.__valor
