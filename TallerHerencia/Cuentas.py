class Cuentas:
    def __init__(self, cuenta, saldo):
        self.cuenta = cuenta
        self.saldo = saldo

    def mostrar_info(self):
        print(f"Cuenta: {self.cuenta}")
        print(f"Saldo: {self.saldo}")

class CuentaAhorro(Cuentas):
    def __init__(self, cuenta, saldo, tasa_interes):
        super().__init__(cuenta, saldo)
        self.tasa_interes = tasa_interes

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Interes: {self.tasa_interes}")

class CuentaCorriente(Cuentas):
    def __init__(self, cuenta, saldo, sobregiro):
        super().__init__(cuenta, saldo)
        self.sobregiro = sobregiro

    def mostrar_info(self):
        super().mostrar_info()
        print(f"SobreGiro: {self.sobregiro}")

class CuentaInversion(Cuentas):
    def __init__(self, cuenta, saldo, rendimiento):
        super().__init__(cuenta, saldo)
        self.rendimiento = rendimiento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Rendimiento: {self.rendimiento}")  

if __name__ == "__main__":
    ahorro = CuentaAhorro("001", 1500.0, 0.03)
    corriente = CuentaCorriente("002", 500.0, 200.0)
    inversion = CuentaInversion("003", 10000.0, 0.08)
    print("=========================================")
    print("Detalles de las cuentas:")
    print("=========================================")
    print("Cuenta de Ahorro:")
    ahorro.mostrar_info()
    print("=========================================")
    print("\nCuenta Corriente:")
    corriente.mostrar_info()
    print("=========================================")  
    print("\nCuenta de Inversion:")
    inversion.mostrar_info()