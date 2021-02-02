from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimalModelTestCase(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal = 'Leao',
            predador = 'Sim',
            venenoso = 'Nao',
            domestico = 'Nao'
        )

    def test_animal_cadastrado_com_caracteristicas(self):
        """Teste que verifica se o animal esta cadastrado com suas respectivas caracteristicas"""
        self.assertEqual(self.animal.nome_animal, 'Leao')