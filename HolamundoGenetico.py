#Monroy Velázquez Alejandra Sarahí
#Inteigencia Artificial Grupo 2
import random

#Esta funcion genera una cadena aleatoria de igual tamaño a la cadena que el usuario introdujo, y la guarda en una lista
def cadenag(tamaño):
    lista = [] 
    while len(lista) < tamaño:
        lista.extend(random.sample(abc, tamaño))
    return ''.join(lista)

#Esta funcion suma 1 si el caracter mutado es igual en posicion al caracter correspondiente a la cadena introducida
def pos(lugar):
    return sum(1 for caracter, caOriginal in zip(cadena, lugar)
               if caracter == caOriginal)

#Esta funcion cambia o muta aleatoriamente la cadena que recibe
def mutar(cadenam):
    i = random.randrange(0, len(cadenam))
    mut = list(cadenam)
    newmut, aux = random.sample(abc, 2)
    if newmut == mut[i]: 
      mut[i] = aux
    else:
      newmut
    return ''.join(mut)

#Primeramente tenemos una cadena que contiene todos los caracteres con los que se hará la mutación de la cadena a la cual se quiere llegar.
abc = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

#Se imprime un diseño sencillo, se pide y se guarda la cadena objetivo.
print("\t\t**Algoritmo Genetico**\n")
print("Escribe una cadena:")
print("(Por ejemplo: Hola Mundo)")
cadena = input()
print("\n\n")

#Se inicializan las variables y se imprime la cadena con la que vamos a comenzar
cadenap = cadenag(len(cadena))
caracterp = pos(cadenap)
print(cadenap)

#Se hacen cuantas iteraciones señalen, mutando las cadenas conforme se van encontrando los caraceres que correspondan a la cadena que el usuario introdujo, mientras que a su vez se van imprimiendo.
while True:
    cadenam = mutar(cadenap)
    if caracterp >= pos(cadenam):
        continue
    print(cadenam)
    if pos(cadenam) >= len(cadenap):
        break
    caracterp = pos(cadenam)
    cadenap = cadenam