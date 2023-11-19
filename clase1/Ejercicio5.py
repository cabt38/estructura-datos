class Vehiculo:
    def __init__(self, nivel_combustible):
        self.nivel_combustible = nivel_combustible
        self.encendido = False

    def encender(self):
        if self.encendido:
            print("El vehículo está encendido.")
        else:
            print("Encendiendo el vehículo.")
            self.encendido = True

    def apagar(self):
        if not self.encendido:
            print("El vehículo está apagado.")
        else:
            print("Apagando el vehículo.")
            self.encendido = False

    def avanzar(self, distancia):
        if not self.encendido:
            print("El vehículo está apagado. Por favor enciéndalo.")
        else:
            consumo = distancia * 0.3
            if self.nivel_combustible >= consumo:
                self.nivel_combustible -= consumo
                print(f"Avanzando {distancia} km. Nivel de combustible restante: {self.nivel_combustible:.2f} litros")
                if self.nivel_combustible <= 10:
                    print("Nivel de combustible bajo.")
                if self.nivel_combustible <= 0:
                    print("El vehículo se quedó sin combustible. Por favor repostar el vehiculo")
                    self.apagar()
            else:
                print("No hay suficiente combustible para completar la distancia requerida.")


vehiculo = Vehiculo(nivel_combustible=50)

vehiculo.encender()

vehiculo.avanzar(0)
vehiculo.avanzar(10)
vehiculo.avanzar(20)

vehiculo.apagar()