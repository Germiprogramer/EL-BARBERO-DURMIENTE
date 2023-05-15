from clases import Barbero, Cliente, time, random
from queue import Queue
from threading import Semaphore

def iniciar_problema(num_barberos):
    cola = Queue()
    semaforo = Semaphore(num_barberos)
    barberos = []
    for i in range(num_barberos):
        barbero = Barbero(f"Barbero {i+1}", cola, semaforo)
        barbero.start()
        barberos.append(barbero)
    n = 0
    while True:
        n += 1
        cliente = Cliente(cola, f"Cliente {n}", semaforo)
        cliente.start()
        time.sleep(random.randint(1, 3))

