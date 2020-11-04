import vogais

import unittest

class TestMaximoMethods(unittest.TestCase):

    def test_vogal_a(self):
        self.assertEqual(vogais.vogal('a'), True)

    def test_vogal_A(self):
        self.assertEqual(vogais.vogal('A'), True)

    def test_vogal_casa(self):
        self.assertEqual(vogais.vogal('casa'), False)

if __name__ == '__main__':
    unittest.main()