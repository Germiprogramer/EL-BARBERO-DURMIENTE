import time
import random
from threading import Thread

class Barbero(Thread):
    def __init__(self, nombre, cola, semaforo):
        Thread.__init__(self)
        self.nombre = nombre
        self.cola = cola
        self.estado = "dormido"
        self.semaforo = semaforo

    def run(self):
        while True:
            if self.cola.empty():
                self.estado = "dormido"
            else:
                self.cola.get()
                self.semaforo.release()
                self.estado = "despierto"
                print(f"{self.nombre} cortando el pelo")
                time.sleep(random.randint(3, 6))
                print(f"{self.nombre} terminó de cortar el pelo")
                self.cola.task_done()

class Cliente(Thread): 
    def __init__(self, cola, nombre, semaforo):
        Thread.__init__(self)
        self.cola = cola
        self.nombre = nombre
        self.semaforo = semaforo

    def run(self):
        self.cola.put(1)
        self.semaforo.acquire()
        print(f"{self.nombre} esperando")
        time.sleep(random.randint(1, 5))