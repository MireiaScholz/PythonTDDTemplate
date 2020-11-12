import unittest  
from range_parser import parseRange

# Creamos una clase heredando de TestCase
class TestRangeParser(unittest.TestCase):  

    # Creamos una prueba para probar un valor inicial
    def test_example(self):
        self.assertEqual("Hello World", parseRange("Hola Mundo"))