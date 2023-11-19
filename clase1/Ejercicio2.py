"""
segundo punto: Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo. 
Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado
"""


class Vehiculo:
    def __init__(self, combustible, marca):
        self.combustible = combustible
        self.marca = marca

    def encender(self):
        return "el vehiculo de marca {} se ha encendido".format(self.marca)

    def arrancar(self):
        return (
            "el vehiculo de marca {} ha iniciado la marcha con combustible {}".format(
                self.marca, self.combustible
            )
        )


class Moto(Vehiculo):
    def cilindraje(self, cilin):
        return "el tipo de combustible de la moto es {}, su marca es {} y el cilindraje que esta tiene es {}".format(
            self.combustible, self.marca, cilin
        )


class Carro(Vehiculo):
    def motor(self, num_motor):
        return "el tipo de combustible que consume el automovil es {}, su marca es {} y el tipo de motor que esta tiene es {}".format(
            self.combustible, self.marca, num_motor
        )


moto = Moto("extra", "Yamaha")
print(moto.cilindraje(250))

carro = Carro("diesel", "chevrolet")
print(carro.motor("V8"))
