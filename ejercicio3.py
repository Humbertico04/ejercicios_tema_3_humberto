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
            nombre=nombre[0].capitalize() + nombre[1:]
            naves = Nave(nombre, largo, tripulacion, pasajeros)
            lista.append(naves)

    @staticmethod
    def mergesort(lista_naves, categoria):
        if len(lista_naves) <= 1:
            return lista_naves
        else:
            medio = len(lista_naves) // 2
            izquierda = Naves.mergesort(lista_naves[:medio], categoria)
            derecha = Naves.mergesort(lista_naves[medio:], categoria)
            return Naves.merge(izquierda, derecha, categoria)

    @staticmethod
    def merge(izquierda, derecha, categoria):
        lista_mezclada = []
        i, j = 0, 0
        while i < len(izquierda) and j < len(derecha):
            nave1 = izquierda[i]
            nave2 = derecha[j]

            if getattr(nave1, categoria) < getattr(nave2, categoria):
                lista_mezclada.append(nave1)
                i += 1
            else:
                lista_mezclada.append(nave2)
                j += 1

        lista_mezclada += izquierda[i:]
        lista_mezclada += derecha[j:]
        return lista_mezclada
    
    @staticmethod
    def mostrar_naves(lista_naves):
        for nave in lista_naves:
            print(nave)
    
    @staticmethod
    def mostrar_nave(nombre):
        for nave in Naves.lista:
            if nave.nombre == nombre:
                print(nave)

    @staticmethod
    def mayores(lista_naves, cantidad, categoria):
        lista_naves = Naves.mergesort(lista_naves, categoria)
        lista_naves.reverse()
        return lista_naves[:cantidad]
    
    @staticmethod
    def filtro(lista_naves, filtro):
        lista_filtrada = []
        for nave in lista_naves:
            if nave.nombre.startswith(filtro):
                lista_filtrada.append(nave)
        return lista_filtrada

    @staticmethod
    def minimos(lista_naves, min, categoria):
        if categoria == "nombre":
            return "No se puede filtrar por minimo en nombre"
        lista_naves = Naves.mergesort(lista_naves, categoria)
        i = 0
        for nave in lista_naves:
            if getattr(nave, categoria) >= min:
                # crear una sublista con los elementos desde el minimo hasta el final
                return lista_naves[i:]
            i += 1

    @staticmethod
    def extremos(lista_naves, categoria):
        lista_naves = Naves.mergesort(lista_naves, categoria)
        minimo = lista_naves[0]
        maximo = lista_naves[-1]
        return minimo, maximo

def main():
    naves = Naves.lista
    naves_ordenadas_nombre = Naves.mergesort(naves, "nombre")
    naves_ordenadas_largo = Naves.mergesort(naves_ordenadas_nombre, "largo")
    naves_ordenadas_tripulacion = Naves.mergesort(naves_ordenadas_nombre, "tripulacion")
    naves_ordenadas_pasajeros = Naves.mergesort(naves_ordenadas_nombre, "pasajeros")

    print("Ordenadas por nombre:")
    Naves.mostrar_naves(naves_ordenadas_nombre)

    print("\nOrdenadas por largo:")
    Naves.mostrar_naves(naves_ordenadas_largo)

    print("\nOrdenadas por tripulación:")
    Naves.mostrar_naves(naves_ordenadas_tripulacion)


    print("\nOrdenadas por pasajeros:")
    Naves.mostrar_naves(naves_ordenadas_pasajeros)

    print("\nInformación del Halcón Milenario y la Estrella de la Muerte:")
    Naves.mostrar_nave("Millennium Falcon")
    Naves.mostrar_nave("Death Star")

    print("\nLas cinco naves con mayor cantidad de pasajeros:")
    Naves.mostrar_naves(Naves.mayores(naves, 5, "pasajeros"))

    print("\nLa nave que requiere mayor cantidad de tripulación:")
    Naves.mostrar_naves(Naves.mayores(naves, 1, "tripulacion"))

    print("\nNaves que comienzan con AT:")
    Naves.mostrar_naves(Naves.filtro(naves, "AT"))

    print("\nNaves que pueden llevar seis o más pasajeros:")
    Naves.mostrar_naves(Naves.minimos(naves, 6, "pasajeros"))

    print("\nInformación de la nave más pequeña y la más grande:")
    minimo, maximo = Naves.extremos(naves, "largo")
    print(f"Nave más pequeña: {minimo}")
    print(f"Nave más grande: {maximo}")

if __name__ == "__main__":
    main()