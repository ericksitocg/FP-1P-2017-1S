#Autor Erick Humberto Cordova Gavilanes
import numpy as np
import random as rd
#Tema 1
"""
Ingrese las palabras a calificar: CAS*A*,S*ASTR*E*,R*EY*,A*ZOTE*
Las calificaciones de las palabras son:
casa: 8
sastre: 9
rey: 11
azote: 16
La palabra con mayor puntaje es AZOTE (16 puntos).

"""

print("Tema 1\n")
L_letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
L_puntajes = [1,3,3,2,1,4,2,4,1,9,5,1,3,1,1,3,10,1,1,1,1,4,4,9,4,10]

palabra = input("Ingrese la palabra a calificar: ")
L_palabras = palabra.split(",")

L_palabras_limpias = []
L_puntaje_palabra = []
for pal in L_palabras:
    puntaje_palabra = 0
    palabra_limpia = ""
    for i in range(len(pal)):#usando el i in range accedemos al siguiente
        letra = pal[i]
        if letra.isupper() and letra!= "*":
            puntaje = L_puntajes[L_letras.index(letra)]
            if i != len(pal) -1 and pal[i + 1] == "*":
                puntaje*=2
            puntaje_palabra+=puntaje
            palabra_limpia+=letra.lower()
    L_palabras_limpias.append(palabra_limpia)
    L_puntaje_palabra.append(puntaje_palabra)

print("Las calificaciones de las palabras son: ")
for i in range(len(L_puntaje_palabra)):
    print("%s: %d"%(L_palabras_limpias[i],L_puntaje_palabra[i]))
ind_maxima_puntuacion = L_puntaje_palabra.index(max(L_puntaje_palabra))
print("La palabra con mayor puntaje es %s ( %d puntos )"%(L_palabras_limpias[ind_maxima_puntuacion].upper(),L_puntaje_palabra[ind_maxima_puntuacion]))

#Tema 2
print("Tema 2\n")

"""
Popularidad = número de suscriptores
Rentabilidad = ganancias anuales / número de suscriptores
"""
espana = ["elrubiusOMG", "VEGETTA777","Pablo Alborán"]
ecuador = ["enchufetvLIVE", "Kreizivoy", "Ecuavisa" ]
mexico = ["Yuya", "Werevertumorro","CaELiKe" ]

L = [[24771906,18451280,78493,133538,18554394,13548964],[5477807839,7046108694,798122,21104851,1967543913,2034702069],[21900,45500,36,156,6700,12200],[262800,546000,430,1900,80000,12200]]
M = np.array(L)

print(M)

#Tema 3
print("Tema 3")
"""
a) Dada la siguiente lista L = [ 12, 9 , 1, 3, 2, 10, 20, 5, ...]
Genere 3 posiciones aleatorias de tal manera que los valores correspondientes sumen al menos 20. Al
final imprima la suma de los 3 valores seleccionados aleatoriamente.
"""
L = [ 12, 9 , 1, 3, 2, 10, 20, 5]
suma = 0
while not suma >= 20:
    n_1 = L[rd.randint(0,len(L) - 1)]
    n_2 = L[rd.randint(0,len(L) - 1)]
    n_3 = L[rd.randint(0,len(L) - 1)]

    suma = n_1 + n_2 + n_3
print("La suma es %s"%suma)

"""
b) Dada la siguiente lista:
¿Qué imprime el siguiente código?
"""
stars=['Potter', 'Ron Weasley', 'Dumbledore', 'Hermione Granger','Hagrid','Voldemort']

print(stars[-4:-2])
print( stars[3][0:stars[3].find(" ")] + stars[1][3:] )
