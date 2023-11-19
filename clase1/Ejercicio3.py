"""
La clase Vehiculo, debe tener una propiedad llamada tipo (esta contendrá el ipo de vehiculo - 
Carro o Moto -), esta propiedad debe ser seteada al momento de instanciar la clase Carro o Moto
 y al momento de imprimir el objeto debe indicar el tipo de vehiculo junto con el texto mostrado enteriormente 
"""

class Vehiculo:

    marca: str
    Combustible: str
    tipo: str

    def __init__(self,marca,combustible):
        self.marca = marca
        self.combustible = combustible

    def encernder(self):
        pass
    def arrancar(self):
        pass

    def __str__(self):
        return "El vehiculo tipo {} {} necesita gasolina {} para operar".format(self.tipo, self.marca, self.combustible)
    
class Moto(Vehiculo):
    def __init__(self,marca,combustible):
        super().__init__(marca,combustible)
        self.tipo = "Moto"

class Carro(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible) 
        self.tipo = 'Carro'

print("-"*45)
carro = Carro('Mazda', 'Extra')
print(carro)

moto = Moto('Suzuki', 'Corriente')
print(moto)
print("-"*45)