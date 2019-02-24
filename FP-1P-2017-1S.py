#Autor Erick Humberto Cordova Gavilanes
import numpy as np
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