class Nodo:
    
    # Armazena um dado e uma referência ao próximo nodo:
    def __init__(self, dado=0, nextnodo=None): 
        self.dado = dado
        self.proximo = nextnodo

    # Representação do Nodo:
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
    
# Armazena o topo da pilha:
class Pilha:
    def __init__(self):
        self.topo = None
    
    def __repr__(self):
        return "[" + str(self.topo) + "]"
    
    def insere(self, newdado):
        newnodo = Nodo(newdado)
        newnodo.proximo = self.topo
        self.topo = newnodo
    
    def remove(self):
        assert self.topo is not None, "não foi possível remover o valor de uma pilha vazia"
        valor = self.topo.dado
        self.topo = self.topo.proximo
        return valor
    
# Retorna a lista invertida:
def printinversa(numeros):
    pilha = Pilha()
    
    for numero in numeros:
        pilha.insere(numero)
    
    numeros_invertidos = []
    while pilha.topo is not None:
        numeros_invertidos.append(pilha.remove())
    
    return numeros_invertidos

numeros = [1.5, 2.3, 3.8, 4.0, 5.7]
resultado = printinversa(numeros)
print(f'na ordem inversa o resultado fica assim: {resultado}')
