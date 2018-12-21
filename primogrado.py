#helloworld

#primo grado.py

#Algoritmo che risolve equazioni di primo grado nella forma "aX+b=0".

a = input("Inserisci il valore dell'incognita: ") #Input dell'incognita
a = int(a) #Cast al tipo "int" (intero)
b = input("Inserisci il valore del termine noto: ") #Input del termine noto
b = int(b) #Cast al tipo "int" (intero)
#Costrutto "if...else" (se...altrimenti) per la risoluzioni dell'equazione:
if a==0 and b==0: #Alternativa nel caso in cui entrambi i valori inserit siano pari a 0:
    print("L'equazione e' indeterminata: ammette infinite soluzioni.") #Stampa della soluzione per questa alternativa
elif a==0: #Alternativa nel caso in cui l'incognita sia pari a 0:
    print("L'equazione e' impossibile: non ammette soluzioni") #Stampa della soluzione per questa alternativa
else: #Alternativa in cui entrambi i valori inseriti siano diversi da 0:
    x = -b / a #Calcolo della soluzione
    print("L'equazione ammette soluzione:", x) #Stampa della soluzione per questa alternativa