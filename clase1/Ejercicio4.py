class Vehiculo:

    tipo=str
    marca=str
    combustible=str
    
    def __init__(self, tipo, marca, combustible):
        self.tipo = tipo
        self.marca = marca
        self.combustible = combustible

    def encender(self):
        if self.validar_combustible():
            print("El {} {} se ha encendido.".format(self.tipo, self.marca))
        else:
            print("¡Advertencia! El {} {} necesita ir a la gasolinera.".format(self.tipo, self.marca))

    def arrancar(self):
        pass

    def validar_combustible(self):
        nivel_minimo = 0.1  # 10% del tanque
        return self.combustible >= nivel_minimo

    def __str__(self):
        return "El {} {} necesita {} para operar".format(self.tipo, self.marca, self.combustible)

class Moto(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__("Moto", marca, combustible)

class Carro(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__("Carro", marca, combustible)

moto = Moto('Suzuki', 0.08)  # Nivel de combustible por debajo del 10%
moto.encender()

carro = Carro('Mazda', 0.15)  # Nivel de combustible por encima del 10%
carro.encender()
