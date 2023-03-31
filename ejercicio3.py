# Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de las que conocemos su nombre, largo, 
# tripulación y cantidad de pasajeros, desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:

# realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;
# mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
# determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
# indicar cuál es la nave que requiere mayor cantidad de tripulación;
# mostrar todas las naves que comienzan con AT;
# listar todas las naves que pueden llevar seis o más pasajeros;
# mostrar toda la información de la nave más pequeña y la más grande.

import csv

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
            naves = Nave(nombre.capitalize(), largo, tripulacion, pasajeros)
            lista.append(naves)

    @staticmethod
    def mergesort(lista_naves, attr):
        if len(lista_naves) <= 1:
            return lista_naves
        else:
            medio = len(lista_naves) // 2
            izquierda = Naves.mergesort(lista_naves[:medio], attr)
            derecha = Naves.mergesort(lista_naves[medio:], attr)
            return Naves.merge(izquierda, derecha, attr)

    @staticmethod
    def merge(izquierda, derecha, attr):
        lista_mezclada = []
        i, j = 0, 0
        while i < len(izquierda) and j < len(derecha):
            nave1 = izquierda[i]
            nave2 = derecha[j]

            if getattr(nave1, attr) < getattr(nave2, attr):
                lista_mezclada.append(nave1)
                i += 1
            else:
                lista_mezclada.append(nave2)
                j += 1

        lista_mezclada += izquierda[i:]
        lista_mezclada += derecha[j:]
        return lista_mezclada

naves = Naves.lista
naves_ordenadas_nombre = Naves.mergesort(naves, "nombre")
naves_ordenadas_largo = Naves.mergesort(naves, "largo")
naves_ordenadas_tripulacion = Naves.mergesort(naves, "tripulacion")
naves_ordenadas_pasajeros = Naves.mergesort(naves_ordenadas_nombre, "pasajeros")

print("Ordenadas por nombre:")
for nave in naves_ordenadas_nombre:
    print(nave)

print("\nOrdenadas por largo:")
for nave in naves_ordenadas_largo:
    print(nave)

print("\nOrdenadas por tripulación:")
for nave in naves_ordenadas_tripulacion:
    print(nave)

print("\nOrdenadas por pasajeros:")
for nave in naves_ordenadas_pasajeros:
    print(nave)
