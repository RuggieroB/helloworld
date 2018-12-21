#helloworld

#sfera.py

#Algoritmo che ricevuto in input il raggio di una sfera, ne calcola superficie e volume.

import math #Libreria "math" (matematica)
raggio = input("Inserisci il raggio della sfera: ") #Input del raggio della sfera
raggio = int(raggio) #Cast al tipo "int" (intero)
superficie = 4 * math.pi * raggio * raggio #Calcolo della superficie della sfera
volume = 4 / 3 * math.pi * raggio * raggio * raggio #Calcolo del volume della sfera
print("La sfera di raggio",raggio,"ha superficie:",superficie,"e volume:",volume) #Stampa del valore della superficie e del volume della sfera
