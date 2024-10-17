# index.py

from Agenda import Agenda
from viagem.src.main.python.PlanejamentoViagem import PlanejamentoViagem

def main():
    agenda = Agenda()
    
    # Criação de planejamentos de viagem
    viagem1 = PlanejamentoViagem("Praia de Copacabana", "09:00", "20/12/2024", "João", 1000.00)
    viagem2 = PlanejamentoViagem("Serra Gaúcha", "08:00", "22/12/2024", "Maria", 1500.00)
    viagem3 = PlanejamentoViagem("Foz do Iguaçu", "10:00", "25/12/2024", "Joaquim", 2000.00)
    
    # Adicionando os planejamentos à agenda
    agenda.createPlanejamento(viagem1)
    agenda.createPlanejamento(viagem2)
    agenda.createPlanejamento(viagem3)

    # Lendo e exibindo os planejamentos
    planejamentos = agenda.readPlanejamentos()
    print("Planejamentos de viagem:")
    for viagem in planejamentos:
        print(viagem)

    # Atualizando um planejamento
    viagem4 = PlanejamentoViagem("Viagem de Aniversário", "15:00", "30/12/2024", "Eduardo", 1200.00)
    agenda.updatePlanejamento(1, viagem4)

    # Lendo e exibindo os planejamentos após a atualização
    planejamentos = agenda.readPlanejamentos()
    print("\nPlanejamentos de viagem após atualização:")
    for viagem in planejamentos:
        print(viagem)

    # Removendo um planejamento
    agenda.deletePlanejamento(1)

    # Lendo e exibindo os planejamentos após a exclusão
    planejamentos = agenda.readPlanejamentos()
    print("\nPlanejamentos de viagem após exclusão:")
    for viagem in planejamentos:
        print(viagem)

if __name__ == "__main__":
    main()
