"""
vamos a crear una funcion recursiva en donde se creen por un parametro un cierto numero de nodos
luego crear otra funcion recursiva donde muestre una lista con el numero de nodos que se crearon
y por ultimo dentro de los nodos debe haber un dato aleatorio, este debe ser llamado desde la biblioteca random y debemos decirle que nos pase un numero entero de la siguente manera:::: numero = random.randint()
"""
import random


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.apuntador = None


def nodos_creados(n):
    if n <= 0:
        return None
    else:
        num_random = random.randint(1, 15)
        llamar_nodo = Nodo(num_random)
        llamar_nodo.apuntador = nodos_creados(n - 1)
        return llamar_nodo


def mostrar_los_nodos(nodo):
    if nodo is None:
        return []
    else:
        return [nodo.dato] + mostrar_los_nodos(nodo.apuntador)


numero_nodos = int(input("ingrese el numero de nodos que quiere crear: "))
nodoscreados = nodos_creados(numero_nodos)
lista_de_nodos = mostrar_los_nodos(nodoscreados)
print(lista_de_nodos)
