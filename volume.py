#helloworld

#volume.py

#Algoritmo che in base ad una scelta dell'utente, calcola il valume di un cubo (in base al lato inserito in input) o quello di una sfera (in base al raggio inserito in input).

import math #Libreria "math" (matematica)

scelta = input("Scegli tra cubo e sfera: digita \"0\" per il cubo, \"1\" per la sfera: ") #Input per la scelta tra cubo e sfera
scelta = int(scelta) #Cast al tipo "int" (intero)
#Costrutto "if...else" (se...altrimenti) per definire la scelta dell'utente:
if scelta==0: #Alternativa nel caso in cui l'utente abbia scelto il cubo:
    lato = input("Inserisci il lato del cubo: ") #Input del raggio del cubo
    lato = int(lato) #Cast al tipo "int" (intero)
    volume = lato * lato * lato #calcolo del volume del cubo
    print("Il cubo di lato",lato,"ha volume",volume) #Stampa del volume del cubo.
elif scelta==1: #Alternativa nel caso in cui l'utente abbia scelto la sfera:
    raggio = input("Inserisci il raggio della sfera: ") #Input del raggio della sfera
    raggio = int(raggio) #Cast al tipo "int" (intero)
    volume = 4/3 * math.pi * raggio * raggio * raggio #Calcolo del volume della sfera
    print("La sfera di raggio",raggio,"ha volume",volume) #Stampa del volume della sfera
else: 
    print("Scelta non valida!") #Alternativa con messaggio di errore in caso di scelta non valida