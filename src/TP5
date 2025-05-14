import os
import math

# 1. **Cadena de Responsabilidad**


class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, number):
        if self.next_handler:
            self.next_handler.handle(number)


class PrimeHandler(Handler):
    def handle(self, number):
        if self.is_prime(number):
            print(f"Número primo consumido: {number}")
        else:
            super().handle(number)

    def is_prime(self, number):
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True


class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"Número par consumido: {number}")
        else:
            super().handle(number)


class UnusedHandler(Handler):
    def handle(self, number):
        print(f"Número {number} no consumido.")


# 2. **Patrón Iterator**

class StringIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1
            return char
        raise StopIteration

    def reverse_iter(self):
        for char in reversed(self.text):
            yield char


# 3. **Patrón Observer**

class Observer:
    def update(self, message):
        pass


class ConcreteObserver(Observer):
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, message):
        if message == self.observer_id:
            print(f"Observer {self.observer_id} ha detectado su ID emitido.")


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


# 4. **Modificación en IS2_taller_scanner.py**

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(
            self.stations[self.pos], self.name))


class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate


class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.memories = {
            "AM": ["M1", "M2", "M3", "M4"],  # Memorias para AM
            "FM": ["M1", "M2", "M3", "M4"]   # Memorias para FM
        }
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

        print("Memorías FM:")
        for memory in self.memories["FM"]:
            print(f"Memoria FM: {memory}")

        print("Memorías AM:")
        for memory in self.memories["AM"]:
            print(f"Memoria AM: {memory}")


# 5. **Modificación en IS2_taller_memory.py**

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.history.append(memento)
        if len(self.history) > 4:
            self.history.pop(0)  # Mantener solo los 4 estados más recientes
        return memento

    def undo(self, memento_idx):
        if 0 <= memento_idx < len(self.history):
            memento = self.history[memento_idx]
            self.file = memento.file
            self.content = memento.content


class FileWriterCaretaker:
    def save(self, writer):
        self.obj = writer.save()

    def undo(self, writer, memento_idx=0):
        writer.undo(memento_idx)


# Ejecución de los 5 puntos

if __name__ == "__main__":
    os.system("clear")

    # 1. Cadena de Responsabilidad
    print("Procesando números del 1 al 100:")
    prime_handler = PrimeHandler()
    even_handler = EvenHandler(prime_handler)
    unused_handler = UnusedHandler(even_handler)

    for number in range(1, 101):
        unused_handler.handle(number)

    # 2. Iterator
    print("\nIterando en orden:")
    iterator = StringIterator("Python")
    for char in iterator:
        print(char, end=" ")
    print("\nIterando en reversa:")
    for char in iterator.reverse_iter():
        print(char, end=" ")

    # 3. Observer
    print("\nEmitiendo ID:")
    subject = Subject()
    observer1 = ConcreteObserver("IJKL")
    observer2 = ConcreteObserver("ABCD")
    observer3 = ConcreteObserver("MNOP")
    observer4 = ConcreteObserver("UVWX")

    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)
    subject.attach(observer4)

    subject.notify("IJKL")
    subject.notify("ABCD")
    subject.notify("MNOP")
    subject.notify("UVWX")

    # 4. Scanner de radio
    print("\nCrea un objeto radio y almacena las siguientes acciones:")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()

    # 5. Memoria
    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility("GFG.txt")

    print("\nSe graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content)
    caretaker.save(writer)

    print("\nSe graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content)
    caretaker.save(writer)

    print("\nSe graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content)

    caretaker.undo(writer, memento_idx=0)
    print("\nSe muestra el estado actual")
    print(writer.content)

    caretaker.undo(writer, memento_idx=1)
    print("\nSe muestra el estado actual")
    print(writer.content)
