# Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de las que conocemos su nombre, largo, 
# tripulación y cantidad de pasajeros, desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:

# realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;
# mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
# determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
# indicar cuál es la nave que requiere mayor cantidad de tripulación;
# mostrar todas las naves que comienzan con AT;
# listar todas las naves que pueden llevar seis o más pasajeros;
# mostrar toda la información de la nave más pequeña y la más grande.

import csv, helpers

class Nave:
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = float(largo)
        self.tripulacion = int(float(tripulacion))
        self.pasajeros = int(float(pasajeros))

    def __str__(self):
        return f"{self.nombre} (Largo: {self.largo}, Tripulación: {self.tripulacion}, Pasajeros: {self.pasajeros})"

class Naves:
    lista = []
    with open("naves.csv", newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=',')
        next(reader) # Salta la primera línea
        for nombre, largo, tripulacion, pasajeros in reader:
            naves = Nave(nombre, largo, tripulacion, pasajeros)
            print(naves)
            lista.append(naves)

    @staticmethod
    def mergesort(lista_naves):
        if len(lista_naves) <= 1:
            return lista_naves
        else:
            medio = len(lista_naves) // 2
            izquierda = Naves.mergesort(lista_naves[:medio])
            derecha = Naves.mergesort(lista_naves[medio:])
            return Naves.merge(izquierda, derecha)

    @staticmethod
    def merge(izquierda, derecha):
        lista_mezclada = []
        i, j = 0, 0
        while i < len(izquierda) and j < len(derecha):
            nave1 = izquierda[i]
            nave2 = derecha[j]

            if nave1.nombre < nave2.nombre or (nave1.nombre == nave2.nombre and nave1.largo > nave2.largo):
                lista_mezclada.append(nave1)
                i += 1
            else:
                lista_mezclada.append(nave2)
                j += 1

        lista_mezclada += izquierda[i:]
        lista_mezclada += derecha[j:]
        return lista_mezclada

naves = Naves.lista

for nave in naves:
    print(nave)