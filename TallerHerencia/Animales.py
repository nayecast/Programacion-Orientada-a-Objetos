class Animales:
    def __init__(self, nombre, edad, tipo_Alimentacion=None):
        self.nombre = nombre
        self.edad = edad
        self.tipo_Alimentacion = tipo_Alimentacion

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        if self.tipo_Alimentacion:
            print(f"Tipo de Alimentación: {self.tipo_Alimentacion}")
        else:
            print("Tipo de Alimentación: No especificado")

class Aves(Animales):
    def __init__(self, nombre, edad, tipo_Alimentacion=None):
        super().__init__(nombre, edad, tipo_Alimentacion)

    def comportamiento_espe(self):
        print(f"{self.nombre} puede volar.")

class Mamiferos(Animales):
    def __init__(self, nombre, edad, tipo_Alimentacion=None):
        super().__init__(nombre, edad, tipo_Alimentacion)

    def comportamiento_espe(self):
        print(f"{self.nombre} amamantan a sus crias")

class Reptiles(Animales):
    def __init__(self, nombre, edad, tipo_Alimentacion=None):
        super().__init__(nombre, edad, tipo_Alimentacion)

    def comportamiento_espe(self):
        print(f"{self.nombre} puede reptar")

if __name__ == "__main__":
    loro = Aves("Aguila", 2)
    leon = Mamiferos("Tigre", 5, "Carnivoro")
    iguana = Reptiles("Lagartija", 3, "Carnivoro")

    print("=== Informacion de los Animales ===")
    print("-----------------------------------")
    loro.mostrar_info()
    loro.comportamiento_espe()
    print("-----------------------------------")
    leon.mostrar_info()
    leon.comportamiento_espe()
    print("-----------------------------------")
    iguana.mostrar_info()
    iguana.comportamiento_espe()