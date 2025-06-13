class Cursos:
    def __init__(self, titulo, duracion, nivel):
        self.titulo=titulo
        self.duracion=duracion
        self.nivel=nivel
    def mostrar_info(self):
        print(f"Curso: {self.titulo}")
        print(f"Duracion: {self.duracion}")
        print(f"Nivel: {self.nivel}")

class VideoCurso(Cursos):
    def __init__(self, titulo, duracion, nivel, num_video):
        super().__init__(titulo, duracion, nivel)
        self.num_video=num_video
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cantidad de videos: {self.num_video}")

class CursoVivo(Cursos):
    def __init__(self, titulo, duracion, nivel, fecha_inicio):
        super().__init__(titulo, duracion, nivel)
        self.fecha_inicio=fecha_inicio
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Fecha de inicio: {self.fecha_inicio}")

class CursoLectura(Cursos):
    def __init__(self, titulo, duracion, nivel, num_paginas):
        super().__init__(titulo, duracion, nivel)
        self.num_paginas=num_paginas
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cantidad de paginas: {self.num_paginas}")

cursos = [
    VideoCurso("Python Avanzado", "40 horas", "Avanzado", 20),
    CursoVivo("Desarrollo Web", "30 horas", "Intermedio", "2023-10-01"),
    CursoLectura("Algoritmos y Estructuras de Datos", "50 horas", "Básico", 300)
]
print("Información de los cursos:")
print("=========================================")
for curso in cursos:
    curso.mostrar_info()
    print("=========================================")      