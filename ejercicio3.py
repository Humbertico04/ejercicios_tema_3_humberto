# Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de las que conocemos su nombre, largo, 
# tripulación y cantidad de pasajeros, desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:

# realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;
# mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
# determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
# indicar cuál es la nave que requiere mayor cantidad de tripulación;
# mostrar todas las naves que comienzan con AT;
# listar todas las naves que pueden llevar seis o más pasajeros;
# mostrar toda la información de la nave más pequeña y la más grande.

class Nave:
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = float(largo)
        self.tripulacion = int(tripulacion)
        self.pasajeros = int(pasajeros)

    def __str__(self):
        return f"{self.nombre} (Largo: {self.largo}, Tripulación: {self.tripulacion}, Pasajeros: {self.pasajeros})"
