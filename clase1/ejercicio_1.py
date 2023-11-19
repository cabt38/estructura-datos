class VEHICULO:
    marca = ""
    combustible = ""

    def encender(self):
        return f"se encendio el veiculo con el combustible {self.combustible}"  # esa f del principio se coloca para que reconozca la funcion que estoy llamando dentro del texto del print

    def arrancar(self):
        pass

    def __init__(self, combustible, marca):
        self.combustible = combustible
        self.marca = marca


carro = VEHICULO(
    "corriente", "mazda"
)  # asi se define un objeto, el nombre que queremos que tengamos = y luego llamamos a la clase y le ponemos los atributos que desemos

print("su marca de carro es " + carro.marca)
print("el combustible que debe de consumir su vehiculo es " + carro.combustible)
print("#" * 25)
print(carro.encender())
