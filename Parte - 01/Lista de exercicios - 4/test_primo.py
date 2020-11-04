import primo

import unittest

class TestMaximoMethods(unittest.TestCase):

    def test_maior_primo_100(self):
        self.assertEqual(primo.maior_primo(100), 97)

    def test_maior_primo_0(self):
        self.assertEqual(primo.maior_primo(0), 2)

    def test_maior_primo_negativo(self):
        self.assertEqual(primo.maior_primo(-2), 2)

if __name__ == '__main__':
    unittest.main()