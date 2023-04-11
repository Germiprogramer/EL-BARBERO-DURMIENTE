from queue import Queue
from threading import Thread, Semaphore
import threading
import time
import tkinter as tk

class Barbero(Thread):
    def __init__(self, cola, semaforo,interfaz, x, y):
        Thread.__init__(self)
        #una queue para los clientes
        self.cola = cola
        self.estado = "dormido"
        self.semaforo = semaforo
        self.interfaz = interfaz
        self.x = x
        self.y = y
        self.estado_label = tk.Label(self.interfaz, text= f"El barbero está {self.estado}", bg="#000000", fg="#ffffff")
        self.estado_label.place(x=self.x, y=self.y)

    def run(self):
        while True:
            if self.cola.empty():
                    self.estado = "dormido"
            
            else: 
                    self.cola.get()
                    self.semaforo.release()
                    self.estado = "despierto"
                    print("Cortando el pelo")
                    time.sleep(3)
                    self.cola.task_done()

class Cliente(Thread): 
    def __init__(self, cola, nombre, semaforo):
        Thread.__init__(self)
        self.cola = cola
        self.nombre = nombre
        self.semaforo = semaforo

    def run(self):
        self.cola.put(1)
        self.semaforo.adquire()
        print(f"{self.nombre} esperando")
        time.sleep(5)

class Interfaz:
    def __init__(self):
        
        self.ventana = tk.Tk()
        self.ventana.title("Barbero")
        self.ventana.geometry("300x300")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="#000000")
        self.ventana.mainloop()
        threading.Thread(target=self.iniciar).start()

    def iniciar(self):
        cola = Queue()
        e = Semaphore(1)
        barbero = Barbero(cola, e, self.ventana ,50, 50)
        barbero.start()
        n = 0
        while True:
            n +=1
            cliente = Cliente(cola, f"Cliente {n}", e)
            cliente.run()
            time.sleep(1)   

if __name__ == "__main__":

    Interfaz()