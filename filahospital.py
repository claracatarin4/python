from collections import deque 

class FilaHospital:
    def __init__(self):
        self.fila = deque()  

    def enqueue(self, item):
        self.fila.append(item)  

    def dequeue(self):
        if self.is_empty():
            return None  
        return self.fila.popleft()  

    def is_empty(self):
        return len(self.fila) == 0  

    def tamanho(self):
        return len(self.fila)  

    def mostrar(self):
        return list(self.fila)  
    
    def reverso(self):
        return self.fila.reverse()
    

if __name__ == "__main__":

    fila_atendimento = FilaHospital()

    fila_atendimento.enqueue("cliente 1")
    fila_atendimento.enqueue("cliente 2")
    fila_atendimento.enqueue("cliente 3")
    fila_atendimento.enqueue("cliente 4")

    print ("fila invertida:", fila_atendimento.reversed())

    print (f"fila inicial:" , fila_atendimento.mostrar())
    
    cliente_atendido = fila_atendimento.dequeue()
    print (f"sendo atendido: {cliente_atendido}")

    print ("fila após atendimento:", fila_atendimento.mostrar())

    fila_atendimento.enqueue("cliente 5")
    fila_atendimento.enqueue("cliente 6")

    print ("fila após adições:", fila_atendimento.mostrar())


    while not fila_atendimento.is_empty():
        cliente_atendido = fila_atendimento.dequeue()
        print(f"atendendo: {cliente_atendido}")

print ("fila após atendimento:", fila_atendimento.mostrar())

