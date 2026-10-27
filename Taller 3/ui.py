from modelo import Cuenta


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero.")


def leer_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debe ingresar un número válido.")


def buscar_cuenta(cuenta_clientes, numero):
    for cuenta in cuenta_clientes:
        if cuenta.numero_cuenta == numero:
            return cuenta
    return None


def crear_cuenta(cuenta_clientes):
    numero = leer_entero("Número de cuenta: ")
    if buscar_cuenta(cuenta_clientes, numero) is not None:
        print("Ya existe una cuenta con ese número.")
        return
    documento = leer_entero("Documento de identidad: ")
    nombre = input("Nombre del cliente: ")
    saldo = leer_decimal("Saldo inicial: ")
    cuenta_clientes.append(Cuenta(numero, documento, nombre, saldo))
    print("Cuenta creada correctamente.")


def depositar(cuenta_clientes):
    numero = leer_entero("Número de cuenta: ")
    cuenta = buscar_cuenta(cuenta_clientes, numero)
    if cuenta is None:
        print("Cuenta no encontrada.")
        return
    monto = leer_decimal("Monto a depositar: ")
    if cuenta.depositar_dinero(monto):
        print(f"Depósito realizado (con retención del 19 %). \nSaldo: {cuenta.saldo:.2f}")
    else:
        print("El monto debe ser mayor que cero.")


def retirar(cuenta_clientes):
    numero = leer_entero("Número de cuenta: ")
    cuenta = buscar_cuenta(cuenta_clientes, numero)
    if cuenta is None:
        print("Cuenta no encontrada.")
        return
    monto = leer_decimal("Monto a retirar: ")
    if cuenta.retirar_dinero(monto):
        print(f"Retiro realizado. Saldo: {cuenta.saldo:.2f}")
    else:
        print("Retiro no permitido: monto inválido o saldo insuficiente.")


def mostrar_cuenta(cuenta_clientes):
    numero = leer_entero("Número de cuenta: ")
    cuenta = buscar_cuenta(cuenta_clientes, numero)
    if cuenta is None:
        print("Cuenta no encontrada.")
    else:
        print("-" * 30)
        cuenta.mostrar_datos()
        print("-" * 30)


def mostrar_todas(cuenta_clientes):
    if not cuenta_clientes:
        print("No hay cuentas registradas.")
        return
    for cuenta in cuenta_clientes:
        print("-" * 30)
        cuenta.mostrar_datos()
        print("-" * 30)


def menu(cuenta_clientes):
    opciones = {
        "1": crear_cuenta,
        "2": depositar,
        "3": retirar,
        "4": mostrar_cuenta,
        "5": mostrar_todas,
    }
    while True:
        print("\n--- MENÚ ---")
        print("1. Crear cuenta")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Mostrar una cuenta")
        print("5. Mostrar todas las cuentas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "0":
            print("Hasta luego.")
            break
        accion = opciones.get(opcion)
        if accion is None:
            print("Opción no válida.")
        else:
            accion(cuenta_clientes)