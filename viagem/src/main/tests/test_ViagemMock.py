import unittest
from unittest.mock import MagicMock, Mock, patch

from viagem.src.main.python.Viagem import Viagem, Agenda

class ViagemTestMock(unittest.TestCase):

    def setUp(self):
        self.agenda = Agenda()
    
    def test_init(self):
        self.assertEqual([], self.agenda.readViagens())

    @patch('Viagem.Agenda.updateViagem')
    def test_updateViagem_with_patch(self, mock_updateViagem):
        viagem_mock = Mock(spec=Viagem)
        self.agenda.createViagem(viagem_mock)
        updated_viagem_mock = Mock(spec=Viagem)
        self.agenda.updateViagem(0, updated_viagem_mock)
        mock_updateViagem.assert_called_with(0, updated_viagem_mock)

    def test_updateViagem_with_Mock(self):
        viagem_mock = Mock(spec=Viagem)
        self.agenda.createViagem(viagem_mock)
        updated_viagem_mock = Mock(spec=Viagem)
        self.agenda.updateViagem(0, updated_viagem_mock)
        self.assertEqual([updated_viagem_mock], self.agenda.readViagens())

    def test_mostrar_valor_viagem(self):
        mock_viagem = Mock(spec=Viagem)
        mock_viagem.mostrar_valor.return_value = 1500.0
        self.agenda.createViagem(mock_viagem)
        self.assertEqual(self.agenda.mostrar_valor_viagem(0), 1500.0)

    def test_not_called(self):
        agenda_mock = Mock(spec=Agenda)
        viagem_mock = Mock(spec=Viagem)
        agenda_mock.createViagem(viagem_mock)
        agenda_mock.reset_mock()
        agenda_mock.createViagem.assert_not_called()

    def test_updateViagem_with_Mock_2(self):
        agenda_mock = Mock(spec=Agenda)
        viagem_mock = Mock(spec=Viagem)
        agenda_mock.createViagem(viagem_mock)
        updated_viagem_mock = Mock(spec=Viagem)
        agenda_mock.updateViagem(0, updated_viagem_mock)
        updated_viagem_mock_2 = Mock(spec=Viagem)
        agenda_mock.updateViagem(0, updated_viagem_mock_2)
        agenda_mock.updateViagem.assert_called()

    def test_updateViagem_with_Mock_falha(self):
        agenda_mock = Mock(spec=Agenda)
        viagem_mock = Mock(spec=Viagem)
        agenda_mock.createViagem(viagem_mock)
        updated_viagem_mock = Mock(spec=Viagem)
        agenda_mock.updateViagem(0, updated_viagem_mock)
        updated_viagem_mock_2 = Mock(spec=Viagem)
        agenda_mock.updateViagem(0, updated_viagem_mock_2)
        
        with self.assertRaises(AssertionError):
            agenda_mock.updateViagem.assert_called_once_with(0, updated_viagem_mock)
        
if __name__ == '__main__':
    unittest.main()