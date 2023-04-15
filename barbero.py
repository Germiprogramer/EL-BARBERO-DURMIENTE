from queue import Queue
from threading import Thread, Semaphore
import threading
import time

class Barbero(Thread):
    def __init__(self,nombre, cola, semaforo):
        Thread.__init__(self)
        #una queue para los clientes
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
                    print(f"{self.nombre} Cortando el pelo")
                    time.sleep(5)
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
        time.sleep(3)

class Problema:
    def __init__(self):
        threading.Thread(target=self.iniciar).start()

    def iniciar(self):
        cola = Queue()
        e = Semaphore(1)
        barbero = Barbero("barbero1", cola, e)
        barbero2 = Barbero("barbero2", cola, e)
        barbero.start()
        barbero2.start()
        n = 0
        while True:
            n +=1
            cliente = Cliente(cola, f"Cliente {n}", e)
            cliente.run()
            time.sleep(1)   

if __name__ == "__main__":

    Problema()