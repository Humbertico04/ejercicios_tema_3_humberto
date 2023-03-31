# Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de las que conocemos su nombre, largo, 
# tripulación y cantidad de pasajeros, desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:

# realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;
# mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
# determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
# indicar cuál es la nave que requiere mayor cantidad de tripulación;
# mostrar todas las naves que comienzan con AT;
# listar todas las naves que pueden llevar seis o más pasajeros;
# mostrar toda la información de la nave más pequeña y la más grande.

import pandas as pd

# importar el archivo csv
df = pd.read_csv('starships.csv')
df2 = pd.read_csv('vehicles.csv')

# filtramos los datos que nos interesan
df = df[['name', 'length', 'crew', 'passengers']]
df2 = df2[['name', 'length', 'crew', 'passengers']]

# unimos los dos dataframes
df = df.append(df2, ignore_index=True)

# guardamos el dataframe en un archivo csv
df.to_csv('naves.csv', index=False)