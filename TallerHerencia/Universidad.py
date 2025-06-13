# Se define la clase base 'Universidad' que contiene atributos comunes a todos los miembros
class Universidad:
    def __init__(self, nombre, id, correo):
        # Constructor que inicializa el nombre, id y correo de una persona en la universidad
        self.nombre = nombre
        self.id = id
        self.correo = correo

    def mostrar_datos(self):
        # Metodo para mostrar los datos comunes
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"Correo: {self.correo}")

# Clase 'Estudiante' que hereda de 'Universidad'
class Estudiante(Universidad):
    def __init__(self, nombre, id, correo, carrera, promedio):
         # Llama al constructor de la clase base (Universidad)
        super().__init__(nombre, id, correo)
        # Agrega atributos propios del estudiante
        self.carrera = carrera
        self.promedio = promedio

    def mostrar_datos(self):
        # Muestra los datos comunes y luego los del estudiante
        super().mostrar_datos()  # Llama al método de la clase base
        print(f"Carrera: {self.carrera}")
        print(f"Promedio: {self.promedio}")

# Clase 'Docente' que también hereda de 'Universidad'
class Docente(Universidad):
    def __init__(self, nombre, id, correo, materia):
        # Inicializa atributos comunes
        super().__init__(nombre, id, correo)
        # Agrega atributo específico del docente
        self.materia = materia

    def mostrar_datos(self):
        # Muestra datos comunes y luego los del docente
        super().mostrar_datos()
        print(f"Materia: {self.materia}")

# Clase 'Administrativo' que hereda de 'Universidad'
class Administrativo(Universidad):
    def __init__(self, nombre, id, correo, departamento):
        # Inicializa atributos comunes
        super().__init__(nombre, id, correo)
        # Atributo propio del administrativo
        self.departamento = departamento

    def mostrar_datos(self): # Muestra los datos comunes y luego los del administrativo
        super().mostrar_datos()
        print(f"Departamento: {self.departamento}")

if __name__ == "__main__":
    # Se crean  de cada tipo de persona en la universidad
    estudi = Estudiante("Juan Villamagua", "F154", "juan11@utpl.edu.ec", "Ingenieria civil", 9.9)
    docen = Docente("Maria Paula", "G857", "paulaG@utpl.edu.ec", "Geologia")
    admin = Administrativo("Diego Jimenez", "T859", "djimenez1@utpl.edu.ec", "Arquitectura")

    # Se muestra la información de cada uno
    print("=== Estudiante ===")
    estudi.mostrar_datos()

    print("\n=== Docente ===")
    docen.mostrar_datos()

    print("\n=== Administrativo ===")
    admin.mostrar_datos()
