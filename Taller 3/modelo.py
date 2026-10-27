class Cuenta:
    RETENCION = 0.19

    def __init__(self, numero_cuenta=0, documento=0, nombre="", saldo=0.0):
        self.__numero_cuenta = numero_cuenta
        self.__documento = documento
        self.__nombre = nombre
        self.__saldo = saldo

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        self.__documento = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    def depositar_dinero(self, monto):
        if monto <= 0:
            return False
        self.__saldo += monto * (1 - Cuenta.RETENCION)
        return True

    def retirar_dinero(self, monto):
        if monto <= 0 or monto > self.__saldo:
            return False
        self.__saldo -= monto
        return True

    def mostrar_datos(self):
        print(f"Número de cuenta: {self.__numero_cuenta}")
        print(f"Documento: {self.__documento}")
        print(f"Nombre: {self.__nombre}")
        print(f"Saldo: {self.__saldo:.2f}")