n = int(input('Digite um número natural: '))

def fizzbuzz(n):
    if n % 5 == 0 and n % 7 == 0:
        return 'fizzbuzz'
    elif n % 5 == 0:
        return 'fizz'
    elif n % 7 == 0:
        return 'buzz'
    else:
        return 'miss'
#faça em outro arquivo separado.
import unittest
from multiplos import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_multiplo_5_e_7(self):
        resultado = fizzbuzz(35)
        self.assertEqual(resultado, "fizzbuzz")

    def test_multiplo_5(self):
        resultado = fizzbuzz(10)
        self.assertEqual(resultado, "fizz")

    def test_multiplo_7(self):
        resultado = fizzbuzz(14)
        self.assertEqual(resultado, "buzz")

    def test_nao_multiplo_5_e_7(self):
        resultado = fizzbuzz(8)
        self.assertEqual(resultado, "miss")

if __name__ == '__main__':
    unittest.main()