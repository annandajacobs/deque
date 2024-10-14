'''
7. Escreva a função deque_sum que retorna a soma dos elementos de um Deque implementado com listas.
'''
class Deque:
    def __init__(self):
        self.items = []

    def addFirst(self, item):
        self.items.insert(0, item)

    def addLast(self, item):
        self.items.append(item)

    def removeFirst(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def removeLast(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    # Função que retorna a soma dos elementos do deque
    def deque_sum(self):
        return sum(self.items)

# Exemplo de uso:
dq = Deque()
dq.addLast(5)
dq.addFirst(3)
dq.addLast(7)

print("Soma dos elementos do deque:", dq.deque_sum())
