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
espana = ["elrubiusOMG", "VEGETTA777"]
ecuador = ["enchufetvLIVE", "Kreizivoy"]
mexico = ["Yuya", "Werevertumorro"]

L = [[24771906,18451280,78493,133538,18554394,13548964],[5477807839,7046108694,798122,21104851,1967543913,2034702069],[21900,45500,36,156,6700,12200],[262800,546000,430,1900,80000,12200]]
M = np.array(L)

"""
1. Nombres de usuarios de los youtubers con mayor rentabilidad en cada país. Tipo de dato de
respuesta: lista de strings
"""
A_suscripciones = M[0,:]
A_ganancias_anuales = M[3,:]

A_rentabilidad = A_ganancias_anuales/A_suscripciones

A_rentabilidad_espana = A_rentabilidad[:len(espana)]
A_rentabilidad_ecuador = A_rentabilidad[len(espana):len(espana) + len(ecuador)]
A_rentabilidad_mexico = A_rentabilidad[len(espana) + len(ecuador):]

mayor_rent_espana = espana[A_rentabilidad_espana.argmax()]
mayor_rent_ecuador = ecuador[A_rentabilidad_ecuador.argmax()]
mayor_rent_mexico = mexico[A_rentabilidad_mexico.argmax()]

L_mejores_rent = [mayor_rent_espana,mayor_rent_ecuador,mayor_rent_mexico]
print(L_mejores_rent)

"""
2. El nombre del país del youtuber con la mayor rentabilidad. Tipo de dato de la respuesta: string
"""
paises = ["españa","ecuador","mexico"]
A_mejores_rent = np.array([A_rentabilidad_espana.max(),A_rentabilidad_ecuador.max(),A_rentabilidad_mexico.max()])
pais_mejor_rent = paises[A_mejores_rent.argmax()]
print(pais_mejor_rent)

"""
Cuántos youtubers de España tienen más suscriptores que el youtuber más popular de América
(Ecuador y México). Tipo de dato de respuesta: valor entero.
"""
A_popularidad = A_suscripciones
A_popularidad_america = A_popularidad[len(espana):]
A_popularidad_espana = A_popularidad[: len(espana)]

mas_popular_america = A_popularidad_america.max()

A_mayores_que_america = A_popularidad_espana[A_popularidad_espana > mas_popular_america]
n_espana_mayor_america = A_mayores_que_america.size

print(n_espana_mayor_america)

"""
4. El número promedio de reproducciones de los youtubers con más de 1’000,000 de suscriptores.
Tipo de dato de respuesta: valor entero.
"""
A_reproducciones = M[1,:]
A_repro_may = A_reproducciones[A_reproducciones > 1000000]
promedio_repro_may = A_repro_may.mean()
print(promedio_repro_may)

"""
5. Cuántos youtubers de Ecuador hay en cada categoría. La categoría se calcula en base a la
siguiente tabla: Tipo de dato de respuesta: ndarray de enteros.
"""

#A_rentabilidad_ecuador = np.array([0.2,0.30,0.40,0.50,0.70])

A_rent_cat1 = A_rentabilidad_ecuador[A_rentabilidad_ecuador<= 0.30]
A_rent_cat2 = A_rentabilidad_ecuador[(A_rentabilidad_ecuador >0.30)&(A_rentabilidad_ecuador <= 0.60)]
A_rent_cat3 = A_rentabilidad_ecuador[A_rentabilidad_ecuador >0.60]

A_rent_categ = np.array([A_rent_cat1.size,A_rent_cat2.size,A_rent_cat3.size])
print(A_rent_categ)

"""
6. El país que generó más ganancias anuales y el país que generó menos ganancias anuales. Luego
muestre el siguiente mensaje reemplazando los datos apropiadamente:
El país X generó Z% más de ganancias que el país Y.

Para calcular el porcentaje utilice la siguiente fórmula.
GX: ganancias anuales del país X
GY: ganancias anuales del país Y (GY es menor que GX)
Porcentaje = (GX - GY) / GY * 100
"""

ind_mayor_ganancia = A_ganancias_anuales.argmax()
ind_menor_ganancia = A_ganancias_anuales.argmin()

mayor_ganancia = A_ganancias_anuales.max()
menor_ganancia = A_ganancias_anuales.min()

pais_mayor_ganancia = ""
pais_menor_ganancia = ""

if ind_mayor_ganancia < len(espana):
    pais_mayor_ganancia = "España"
elif ind_mayor_ganancia >= len(espana) and ind_mayor_ganancia < len(espana) + len(ecuador):
    pais_mayor_ganancia = "Ecuador"
else:
    pais_mayor_ganancia = "Mexico"
print(len(espana))
if ind_menor_ganancia < len(espana):
    pais_menor_ganancia = "España"
elif ind_menor_ganancia >= len(espana) and ind_menor_ganancia < len(espana) + len(ecuador):
    pais_menor_ganancia = "Ecuador"
else:
    pais_menor_ganancia = "Mexico"

print("El país %s generó %.2f %% más de ganancias que el país %s."%(pais_mayor_ganancia,100 *(mayor_ganancia - menor_ganancia)/mayor_ganancia ,pais_menor_ganancia))

#Tema 3
print("Tema 3\n")
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
