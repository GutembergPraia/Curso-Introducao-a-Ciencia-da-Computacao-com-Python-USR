import maximo

import unittest

class TestMaximoMethods(unittest.TestCase):

    def test_x_maior_y(self):
        self.assertEqual(maximo.maximo(2,1), 2)

    def test_y_maior_X(self):
        self.assertEqual(maximo.maximo(10,50), 50)

    def test_x_igual_y(self):
        self.assertEqual(maximo.maximo(5,5), 5)

if __name__ == '__main__':
    unittest.main()