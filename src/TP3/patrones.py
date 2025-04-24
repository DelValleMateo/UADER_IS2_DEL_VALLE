# 1. Clase Singleton para cálculo de factorial
import copy


class Factorial:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Factorial, cls).__new__(cls)
        return cls._instance

    def calcular(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.calcular(n - 1)


# 2. Clase para el cálculo de impuestos (también como Singleton opcional)
class Impuestos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Impuestos, cls).__new__(cls)
        return cls._instance

    def calcular(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012
        total = base_imponible + iva + iibb + contribuciones
        return total


# 3. Clase para representar una hamburguesa con métodos de entrega
class Hamburguesa:
    def entregar(self, metodo):
        metodos = {
            "mostrador": "Entregada en mostrador",
            "retiro": "Retirada por el cliente",
            "delivery": "Enviada por delivery"
        }
        print(metodos.get(metodo, "Método de entrega no válido"))


# 4. Clase Factura con condiciones impositivas
class Factura:
    def __init__(self, importe, condicion_iva):
        self.importe = importe
        self.condicion_iva = condicion_iva

    def mostrar_factura(self):
        print(
            f"Factura: ${self.importe:.2f} - Condición IVA: {self.condicion_iva}")


# 5. Construcción de aviones (Builder Pattern simplificado)
class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar(self):
        print("Avión construido con: " + ", ".join(self.partes))


class ConstructorAvion:
    def construir(self):
        avion = Avion()
        avion.agregar_parte("Body")
        avion.agregar_parte("Turbina izquierda")
        avion.agregar_parte("Turbina derecha")
        avion.agregar_parte("Ala izquierda")
        avion.agregar_parte("Ala derecha")
        avion.agregar_parte("Tren de aterrizaje")
        return avion


# 6. Patrón Prototipo


class Prototipo:
    def clonar(self):
        return copy.deepcopy(self)


class ClasePrototipo(Prototipo):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"Instancia: {self.nombre}")


# 7. Ejemplo de uso del patrón Abstract Factory
# Supongamos una fábrica de interfaces gráficas para diferentes sistemas operativos
class Boton:
    def dibujar(self): pass


class Ventana:
    def mostrar(self): pass


class BotonWindows(Boton):
    def dibujar(self):
        print("Dibujo un botón estilo Windows")


class VentanaWindows(Ventana):
    def mostrar(self):
        print("Muestro una ventana estilo Windows")


class BotonLinux(Boton):
    def dibujar(self):
        print("Dibujo un botón estilo Linux")


class VentanaLinux(Ventana):
    def mostrar(self):
        print("Muestro una ventana estilo Linux")


class GUIFactory:
    def crear_boton(self): pass
    def crear_ventana(self): pass


class WindowsFactory(GUIFactory):
    def crear_boton(self):
        return BotonWindows()

    def crear_ventana(self):
        return VentanaWindows()


class LinuxFactory(GUIFactory):
    def crear_boton(self):
        return BotonLinux()

    def crear_ventana(self):
        return VentanaLinux()


# Ejemplo de uso de Abstract Factory
def construir_gui(factory):
    boton = factory.crear_boton()
    ventana = factory.crear_ventana()
    boton.dibujar()
    ventana.mostrar()
