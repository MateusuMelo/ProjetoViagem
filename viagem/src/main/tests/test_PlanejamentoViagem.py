import unittest

from viagem.src.main.python.PlanejamentoViagem import PlanejamentoViagem
from viagem.src.main.python.Viagem import Viagem


class TestPlanejamentoViagem(unittest.TestCase):

    def test_create_viagem(self):
        planejamento = PlanejamentoViagem()  # Cria um novo planejamento de viagem
        viagem = Viagem("Paris", "15/06/2024", "20/06/2024", 2000.00, "Lazer")  # Cria um objeto Viagem
        planejamento.createViagem(viagem)  # Adiciona a viagem no planejamento
        viagens = planejamento.readViagens()  # Recupera a lista de viagens do planejamento
        self.assertEqual(len(viagens), 1)  # Verifica se há apenas 1 viagem
        self.assertEqual(viagens[0], viagem)  # Verifica se a viagem adicionada é a mesma que foi criada

    def test_update_viagem(self):
        planejamento = PlanejamentoViagem()  # Cria um novo planejamento de viagem
        viagem1 = Viagem("Nova York", "10/07/2024", "20/07/2024", 3000.00, "Negócios")  # Cria um objeto Viagem
        viagem2 = Viagem("Tóquio", "05/08/2024", "15/08/2024", 4000.00, "Lazer")  # Cria um objeto Viagem
        planejamento.createViagem(viagem1)  # Adiciona a viagem no planejamento
        planejamento.createViagem(viagem2)  # Adiciona a viagem no planejamento

        updated_viagem = Viagem("Londres", "01/09/2024", "10/09/2024", 3500.00, "Educação")
        planejamento.updateViagem(0, updated_viagem)  # Atualiza a viagem no índice 0

        viagens = planejamento.readViagens()  # Recupera a lista de viagens do planejamento
        self.assertEqual(viagens[0], updated_viagem)  # Verifica se a viagem foi atualizada corretamente

    def test_delete_viagem(self):
        planejamento = PlanejamentoViagem()  # Cria um novo planejamento de viagem
        viagem1 = Viagem("Rio de Janeiro", "01/11/2024", "05/11/2024", 1500.00, "Lazer")  # Cria um objeto Viagem
        viagem2 = Viagem("Buenos Aires", "10/11/2024", "15/11/2024", 1800.00, "Lazer")  # Cria um objeto Viagem
        planejamento.createViagem(viagem1)  # Adiciona a viagem no planejamento
        planejamento.createViagem(viagem2)  # Adiciona a viagem no planejamento
        
        planejamento.deleteViagem(1)  # Remove a viagem do índice 1
        viagens = planejamento.readViagens()  # Recupera a lista de viagens do planejamento
        self.assertEqual(viagens[0], viagem1)  # Verifica se a primeira viagem restante está correta
        
    def test_read_viagens(self):
        planejamento = PlanejamentoViagem()  # Cria um novo planejamento de viagem
        viagem1 = Viagem("Barcelona", "01/10/2024", "10/10/2024", 2500.00, "Lazer")  # Cria um objeto Viagem
        viagem2 = Viagem("Lisboa", "15/10/2024", "25/10/2024", 2200.00, "Negócios")  # Cria um objeto Viagem
        planejamento.createViagem(viagem1)  # Adiciona a viagem no planejamento
        planejamento.createViagem(viagem2)  # Adiciona a viagem no planejamento
        viagens = planejamento.readViagens()  # Recupera a lista de viagens do planejamento
        self.assertEqual(viagens, [viagem1, viagem2])  # Verifica se a lista retornada está correta

    def test_clear_viagens(self):
        planejamento = PlanejamentoViagem()  # Cria um novo planejamento de viagem
        viagem1 = Viagem("Berlim", "05/12/2024", "15/12/2024", 2700.00, "Lazer")  # Cria um objeto Viagem
        viagem2 = Viagem("Amsterdã", "20/12/2024", "30/12/2024", 2900.00, "Lazer")  # Cria um objeto Viagem
        planejamento.createViagem(viagem1)  # Adiciona a viagem no planejamento
        planejamento.createViagem(viagem2)  # Adiciona a viagem no planejamento
        planejamento.clearViagens()  # Limpa a lista de viagens
        self.assertEqual(planejamento.readViagens(), [])  # Verifica se a lista está vazia após a limpeza

    def test_clear_viagens_not_empty(self):
        planejamento = PlanejamentoViagem()  # Cria um novo planejamento de viagem
        viagem1 = Viagem("Dubai", "01/03/2025", "10/03/2025", 4500.00, "Lazer")  # Cria um objeto Viagem
        viagem2 = Viagem("Sydney", "15/03/2025", "25/03/2025", 4800.00, "Negócios")  # Cria um objeto Viagem
        planejamento.createViagem(viagem1)  # Adiciona a viagem no planejamento
        planejamento.createViagem(viagem2)  # Adiciona a viagem no planejamento
        
        self.assertTrue(planejamento.readViagens())  # Verifica se a lista de viagens não está vazia

        planejamento.clearViagens()  # Limpa a lista de viagens

        self.assertFalse(planejamento.readViagens())  # Verifica se a lista de viagens está vazia
        
    def test_update_viagem_invalid_index(self):
        planejamento = PlanejamentoViagem()
        viagem = Viagem("Cairo", "01/04/2025", "10/04/2025", 3000.00, "Lazer")
        planejamento.createViagem(viagem)

        updated_viagem = Viagem("Roma", "15/04/2025", "25/04/2025", 3200.00, "Negócios")

        with self.assertRaises(IndexError):  # Verifica se a exceção é lançada
            planejamento.updateViagem(50, updated_viagem)  # Índice inválido
            
    def test_delete_viagem_invalid_index(self):
        planejamento = PlanejamentoViagem()
        viagem1 = Viagem("Oslo", "01/05/2025", "10/05/2025", 2800.00, "Educação")
        viagem2 = Viagem("Helsinque", "15/05/2025", "25/05/2025", 3100.00, "Negócios")
        planejamento.createViagem(viagem1)
        planejamento.createViagem(viagem2)

        with self.assertRaises(IndexError):  # Verifica se a exceção é lançada
            planejamento.deleteViagem(20)  # Índice inválido

if __name__ == "__main__":
    unittest.main()
