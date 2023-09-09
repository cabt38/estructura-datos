# la creacion de un nodo comun
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# se definen la clase pila con sus funciones de apilar, imprimir esa pila y eliminar el dato especifico dentro de la pila
class Pila:
    def __init__(self):
        self.superior = None

    def apilar(self, dato):
        print(
            f"Agregando {dato} en la cima de la pila"
        )  # aqui imprimimos los datos almacendos que le pasamos como parametro
        # Si no hay datos, agregamos el valor en el elemento superior y regresamos
        if self.superior == None:
            self.superior = Nodo(dato)
            return
        # en estas tres lineas se crea un objeto que llama al nodo y el dato almacenado y le asignamos la primera posicion de la estructura
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo

    def imprimir(self):
        print("Imprimiendo pila:")
        # Recorrer la pila e imprimir valores
        nodo_temporal = (
            self.superior
        )  # nuevo objeto creado el cual le asignamos el valor del .superior, que vendria siendo la posicion superior en tood momento
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end=",")
            nodo_temporal = nodo_temporal.siguiente
        print("")

    # Funcion que me elimina un dato especifico de la pila
    def eliminar_nodo(self, dato_a_eliminar):
        if self.superior is None:
            print("La pila está vacía, por lo tanto no se puede eliminar ningún nodo")
            return

        # Si el nodo a eliminar está en la parte superior de la pila
        if self.superior.dato == dato_a_eliminar:
            self.superior = self.superior.siguiente
            return

        # Buscar el nodo a eliminar
        nodo_temporal = self.superior
        while (
            nodo_temporal.siguiente is not None
            and nodo_temporal.siguiente.dato != dato_a_eliminar
        ):
            nodo_temporal = nodo_temporal.siguiente

        # Si el nodo a eliminar se encuentra en la pila
        if nodo_temporal.siguiente is not None:
            nodo_temporal.siguiente = nodo_temporal.siguiente.siguiente
        else:
            print(f"No se encontró el dato {dato_a_eliminar} en la pila.")


datos_pila = Pila()

datos_pila.apilar(3)
datos_pila.apilar(8)
datos_pila.apilar(4)
datos_pila.apilar(12)
datos_pila.apilar(5)
datos_pila.apilar(9)


print("Pila original:")
datos_pila.imprimir()

dato_a_eliminar = int(
    input("ingrese el dato a eliminar")
)  # Cambia este valor al dato que deseas eliminar
datos_pila.eliminar_nodo(dato_a_eliminar)

print(f"Pila después de eliminar el dato {dato_a_eliminar}:")
datos_pila.imprimir()

