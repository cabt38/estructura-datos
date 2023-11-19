"""Se importa el modulo random para generar numeros aleatorios"""
import random
"""Se importa el modulo time para medir el tiempo de ejecucion"""
import time

def bubble_sort(arr):
  """
  Ordena una lista usando el método de burbuja.

  Args:
    arr: La lista a ordenar.

  Returns:
    La lista ordenada.
  """

  n = len(arr)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr

def buscar_dato(lista, dato):
    """
    Busca un dato en una lista ordenada usando búsqueda binaria.

    Args:
        lista: La lista ordenada en la que buscar.
        dato: El dato que se desea encontrar.

    Returns:
        La posición del dato si se encuentra en la lista, o -1 si no se encuentra.
    """
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == dato:
            return medio
        elif lista[medio] < dato:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

#Creacion de los datos
inicio = time.time()
random.seed(10)
datos = [random.randint(0, 10000) for _ in range(5000)]
ordenado = bubble_sort(datos)
print(ordenado)
fin = time.time()
print("Tiempo de ejecucion: ", fin-inicio)
print("-"*45)
print("-"*45)
#Buscar los datos
dato_a_buscar = int(input("Ingrese el dato que desea buscar: "))
start = time.time()
posicion = buscar_dato(ordenado, dato_a_buscar)

if posicion != -1:
  print(f"El dato {dato_a_buscar} se encuentra en la posición {posicion}.")
else:
  print(f"El dato {dato_a_buscar} no se encuentra en la lista.")

finish =time.time()
print("Tiempo de ejecucion: ", finish-start)
