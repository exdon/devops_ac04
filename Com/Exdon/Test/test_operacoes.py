from unittest import TestCase
from com.exdon.operacoes import operacoes

class TestOperacaoes(TestCase):
    def setUp(self):
        self.operacoes = operacoes()
    
    def test_multiplicacao(self):
        self.assertEqual(self.operacoes.multiplicacao([5,5]), 25, "Deveria ser 25")
