class Producto: #clase Padre
    def __init__(self, nombre, precio): #constructor que inicializa los atributos en elen el objeto Producto
        self.nombre = nombre #atributos
        self.precio = precio #atributos , precio sin IVA

    def precio_con_iva(self):
        return self.precio * 1.15 #precio con IVA

    def mostrar_info(self):
        return f"{self.nombre} - ${self.precio:.2f} + IVA = ${self.precio_con_iva():.2f}" #retornamos un texto con los datos del producto
                                                                                         #utilizamos un .2f para mostrar dos digitos despues del punto decimal de formato floa
class Televisor(Producto): #subClases
    def __init__(self, nombre, precio, pulgadas):
        super().__init__(nombre, precio) #llamamos al constructor de Producto para inicializar nombre y precio.
        self.pulgadas = pulgadas #guardamos un atributo propio en este caso pulgadas

    def mostrar_info(self):
        return f"{super().mostrar_info()} - {self.pulgadas} pulgadas" #extendemos el metodo Producto y le agrega pulgadas

class Telefono(Producto): #subClases
    def __init__(self, nombre, precio, sim):
        super().__init__(nombre, precio)        #recibe el numero de targetas SIM
        self.sim = sim

    def mostrar_info(self):
        return f"{super().mostrar_info()} - SIM: {self.sim}" #retornamos la informacion + el dato de las SIM

class Laptop(Producto): #subClases
    def __init__(self, nombre, precio, ram):
        super().__init__(nombre, precio)     #recibe la memoria RAM
        self.ram = ram

    def mostrar_info(self):
        return f"{super().mostrar_info()} - RAM: {self.ram}GB" #retornamos la informacion + el dato de la RAM

#factura

productos = [
    Televisor("LG 100\"", 5000, 100),
    Telefono("iPhone 15 ProMax", 1500, 1),
    Laptop("Macbook Pro", 3000, 64)
]
#Utilizamos un for para recorrer toda la lista de productos para mostrar la información de cada uno, incluyendo el precio con IVA
for producto in productos:
    print(producto.mostrar_info())
