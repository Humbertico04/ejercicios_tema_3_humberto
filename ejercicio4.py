# Implementar sobre el TDA polinomio desarrollado previamente las siguientes actividades:

#  restar;
#  dividir;
#  eliminar un término;
#  determinar si un término existe en un polinomio.

class Nodo(object):
    """Clase nodo simplemente enlazo"""
    
    info, sig = None, None

class datoPolinomio(object):
    """Clase dato polinomio"""

    def __init__(self, valor, termino):
        self.valor = valor # exponente
        self.termino = termino # coeficiente

class Polinomio(object):
    """Clase polinomio"""

    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(polinomio, termino, valor):
        """Agrega un termino y su valor al polinomio"""
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if (termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while (actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def modificar_termino(polinomio, termino, valor):
        """Modifica un termino del polinomio"""
        aux = polinomio.termino_mayor
        while (aux is not None and aux.info.termino != termino):
            aux = aux.sig
        aux.info.valor = valor
    
    def obtener_valor(polinomio, termino):
        """Devuelve el valor de un termino del polinomio"""
        aux = polinomio.termino_mayor
        while (aux is not None and aux.info.termino > termino):
            aux = aux.sig
        if (aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0
        
    def mostrar(polinomio):
        """Muestra el polinomio"""
        aux = polinomio.termino_mayor
        pol = ""
        if (aux is not None):
            while (aux is not None):
                signo = " "
                if (aux.info.valor >= 0):
                    signo = "+"
                pol += signo + str(aux.info.valor) + "x^" + str(aux.info.termino)
                aux = aux.sig
        return pol
    
    def sumar(polinomio1, polinomio2):
        """Sumar dos polinomios y devuelve el resultado"""
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado+1):
            total = Polinomio.obtener_valor(polinomio1, i) + Polinomio.obtener_valor(polinomio2, i)
            if (total != 0):
                Polinomio.agregar_termino(paux, i, total)
        return paux
    
    def multiplicar(polinomio1, polinomio2):
        """Multiplica dos polinomios y devuelve el resultado"""
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while (pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while (pol2 is not None):
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if (Polinomio.obtener_valor(paux, termino) != 0):
                    valor += Polinomio.obtener_valor(paux, termino)
                    Polinomio.modificar_termino(paux, termino, valor)
                else:
                    Polinomio.agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    
    def restar(polinomio1, polinomio2):
        """Resta dos polinomios y devuelve el resultado"""
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado+1):
            total = Polinomio.obtener_valor(polinomio1, i) - Polinomio.obtener_valor(polinomio2, i)
            if (total != 0):
                Polinomio.agregar_termino(paux, i, total)
        return paux
    
    def dividir(polinomio1, polinomio2):
        """Divide dos polinomios y devuelve el resultado"""
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while (pol1 is not None):
            termino = pol1.info.termino - polinomio2.grado
            valor = pol1.info.valor / polinomio2.termino_mayor.info.valor
            Polinomio.agregar_termino(paux, termino, valor)
            pol1 = pol1.sig
        return paux
    
    def eliminar_termino(polinomio, termino):
        """Elimina un termino del polinomio"""
        aux = polinomio.termino_mayor
        if aux is not None:
            if aux.info.termino == termino:
                polinomio.termino_mayor = aux.sig
                aux.sig = None
                aux = None
            else:
                while aux.sig is not None and aux.sig.info.termino != termino:
                    aux = aux.sig
                if aux.sig is not None:
                    to_remove = aux.sig
                    aux.sig = aux.sig.sig
                    to_remove.sig = None

    def existe_termino(polinomio, termino):
        """Verifica si existe un termino en el polinomio"""
        aux = polinomio.termino_mayor
        while (aux is not None and aux.info.termino != termino):
            aux = aux.sig
        if (aux is not None):
            return True
        else:
            return False

# PRUEBAS
import unittest 
class TestPolinomio(unittest.TestCase):
    def setUp(self):
        self.polinomio1 = Polinomio()
        self.polinomio2 = Polinomio()
        Polinomio.agregar_termino(self.polinomio1, 3, 5)
        Polinomio.agregar_termino(self.polinomio1, 2, 4)
        Polinomio.agregar_termino(self.polinomio1, 1, 3)
        Polinomio.agregar_termino(self.polinomio1, 0, 2)
        Polinomio.agregar_termino(self.polinomio2, 2, 3)
        Polinomio.agregar_termino(self.polinomio2, 1, 2)
        Polinomio.agregar_termino(self.polinomio2, 0, 1)

    def test_agregar_termino(self):
        self.assertEqual(Polinomio.mostrar(self.polinomio1), "+5x^3+4x^2+3x^1+2x^0")
        self.assertEqual(Polinomio.mostrar(self.polinomio2), "+3x^2+2x^1+1x^0")

    def test_modificar_termino(self):
        Polinomio.modificar_termino(self.polinomio1, 2, 6)
        self.assertEqual(Polinomio.mostrar(self.polinomio1), "+5x^3+6x^2+3x^1+2x^0")

    def test_obtener_valor(self):
        self.assertEqual(Polinomio.obtener_valor(self.polinomio1, 2), 4)
        self.assertEqual(Polinomio.obtener_valor(self.polinomio1, 1), 3)
        self.assertEqual(Polinomio.obtener_valor(self.polinomio1, 0), 2)
        self.assertEqual(Polinomio.obtener_valor(self.polinomio1, 3), 5)

    def test_sumar(self):
        self.assertEqual(Polinomio.mostrar(Polinomio.sumar(self.polinomio1, self.polinomio2)), "+5x^3+7x^2+5x^1+3x^0")

    def test_multiplicar(self):
        self.assertEqual(Polinomio.mostrar(Polinomio.multiplicar(self.polinomio1, self.polinomio2)), "+15x^5+22x^4+22x^3+16x^2+7x^1+2x^0")

    def test_dividir(self):
        polinomio3 = Polinomio()
        Polinomio.agregar_termino(polinomio3, 1, 5)
        Polinomio.agregar_termino(polinomio3, 0, 2)
        self.assertEqual(Polinomio.mostrar(Polinomio.dividir(self.polinomio1, polinomio3)), "+1.0x^2+0.8x^1+0.6x^0+0.4x^-1")

    def test_restar(self):
        self.assertEqual(Polinomio.mostrar(Polinomio.restar(self.polinomio1, self.polinomio2)), "+5x^3+1x^2+1x^1+1x^0")
    
    def test_eliminar_termino(self):
        Polinomio.eliminar_termino(self.polinomio1, 2)
        self.assertEqual(Polinomio.mostrar(self.polinomio1), "+5x^3+3x^1+2x^0")
    
    def test_existe_termino(self):
        self.assertEqual(Polinomio.existe_termino(self.polinomio1, 2), True)
        self.assertEqual(Polinomio.existe_termino(self.polinomio1, 1), True)
        self.assertEqual(Polinomio.existe_termino(self.polinomio1, 0), True)
        self.assertEqual(Polinomio.existe_termino(self.polinomio1, 5), False)

if __name__ == '__main__':
    unittest.main()