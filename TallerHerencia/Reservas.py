class Reservas:
    def __init__(self, numHabitacion, precioNoche):
        self.numHabitacion = numHabitacion
        self.precioNoche = precioNoche
    def mostrar_informacion(self):
        print(f"Habitacion: {self.numHabitacion}")
        print(f"Precio por noche: ${self.precioNoche}")


class HabitacionEstandar(Reservas):
    def __init__(self, numHabitacion, precioNoche, tieneVista):
        super().__init__(numHabitacion, precioNoche)
        self.tieneVista = tieneVista

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo: Estándar")
        print(f"Tiene vista: {'Sí' if self.tieneVista else 'No'}")
        print("--------------------------")


class Suite(Reservas):
    def __init__(self, numHabitacion, precioNoche, tieneJacuzzi):
        super().__init__(numHabitacion, precioNoche)
        self.tieneJacuzzi = tieneJacuzzi    

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo: Suite")
        print(f"Tiene jacuzzi: {"Sí" if self.tieneJacuzzi else "No"}")
        print("--------------------------")


class HabitacionFamiliar(Reservas):
    def __init__(self, numHabitacion, precioNoche, capacidadNiños):
        super().__init__(numHabitacion, precioNoche)
        self.capacidadNiños = capacidadNiños

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Capacidad: {self.capacidadNiños} niños")
        print("--------------------------")
    
if __name__ == "__main__":
    estandar = HabitacionEstandar(101, 80, True)
    suite = Suite(201, 200, True)
    familiar = HabitacionFamiliar(301, 120, 3)

    print("=== Habitacion Estándar ===")
    estandar.mostrar_informacion()
    print("\n=== Suite ===")
    suite.mostrar_informacion()
    print("\n=== Habitacion Familiar ===")
    familiar.mostrar_informacion()