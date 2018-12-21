#helloworld

#paridisp.py

#Algoritmo che ricevuto in input un numero, definirà se sia pari o dispari.

numero = input("Inserisci un numero: ") #Input di un numero
numero = int(numero) #Cast al tipo "int" (intero)
if numero%2 == 0: #Costrutto "if..else (se...altrimenti)" per determinare se il numero inserito sia pari o dispari (varifica attarverso il resto della divisione tra il numero e 2):
    print(numero,"E' pari.") #Stampa dell'avviso che il numero è pari (se il resto della divisione e' pari a 0)
else:
    print(numero,"E' dispari.") #Stampa dell'avviso che il numero è dispari (se il resto della divisione e' diverso da 0)