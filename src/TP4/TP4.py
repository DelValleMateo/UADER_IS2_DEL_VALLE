# 1. Clase Ping con Proxy (Patrón Proxy)
import os


class Ping:
    def execute(self, address):
        if not address.startswith("192."):
            raise ValueError(
                "La dirección IP debe comenzar con '192.' para este método.")
        print(f"Haciendo ping a {address}...")
        os.system(f"ping -c 10 {address}")

    def executefree(self, address):
        print(f"Haciendo ping libre a {address}...")
        os.system(f"ping -c 10 {address}")


class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, address):
        if address == "192.168.0.254":
            print("Redirigiendo ping a www.google.com a través del método ejecutefree...")
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(address)


# 2. Clase para laminadoras (Patrón Bridge)
class Laminadora:
    def producir(self, lamina):
        pass


class TrenLaminador5m(Laminadora):
    def producir(self, lamina):
        print(
            f"Produciendo lámina de 5m con espesor {lamina.espesor} y ancho {lamina.ancho}")


class TrenLaminador10m(Laminadora):
    def producir(self, lamina):
        print(
            f"Produciendo lámina de 10m con espesor {lamina.espesor} y ancho {lamina.ancho}")


class Lamina:
    def __init__(self, espesor=0.5, ancho=1.5, tren=None):
        self.espesor = espesor
        self.ancho = ancho
        self.tren = tren

    def set_tren(self, tren):
        self.tren = tren

    def producir(self):
        if self.tren is None:
            raise ValueError(
                "Debe asignar un tren laminador para producir la lámina.")
        self.tren.producir(self)


# 3. Ensamblado de piezas (Patrón Composite)
class Componente:
    def mostrar(self, nivel=0):
        pass


class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + self.nombre)


class Conjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + self.nombre)
        for componente in self.componentes:
            componente.mostrar(nivel + 1)


# 4. Decorador para operaciones aritméticas (Patrón Decorator)
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        print(self.valor)


class SumarDos:
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        print(self.numero.valor + 2)


class MultiplicarPorDos:
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        print(self.numero.valor * 2)


class DividirPorTres:
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        print(self.numero.valor / 3)


# 5. Ejemplo de Flyweight (para mejorar eficiencia en memoria con objetos similares)
class Flyweight:
    _instances = {}

    @classmethod
    def get_instance(cls, nombre):
        if nombre not in cls._instances:
            cls._instances[nombre] = cls(nombre)
        return cls._instances[nombre]

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"Objeto flyweight: {self.nombre}")
