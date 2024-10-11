class DequeArray:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade  # Array de tamanho fixo
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def append(self, item):
        """Adiciona um item no final do deque."""
        if self.tamanho == self.capacidade:
            raise OverflowError("Deque está cheio")
        self.fila[self.fim] = item
        self.fim = (self.fim + 1) % self.capacidade
        self.tamanho += 1

    def appendleft(self, item):
        """Adiciona um item no início do deque."""
        if self.tamanho == self.capacidade:
            raise OverflowError("Deque está cheio")
        self.inicio = (self.inicio - 1) % self.capacidade
        self.fila[self.inicio] = item
        self.tamanho += 1

    def pop(self):
        """Remove e retorna o item do final do deque."""
        if self.tamanho == 0:
            raise IndexError("Deque está vazio")
        self.fim = (self.fim - 1) % self.capacidade
        item = self.fila[self.fim]
        self.fila[self.fim] = None
        self.tamanho -= 1
        return item

    def popleft(self):
        """Remove e retorna o item do início do deque."""
        if self.tamanho == 0:
            raise IndexError("Deque está vazio")
        item = self.fila[self.inicio]
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return item

    def empty(self):
        """Verifica se o deque está vazio."""
        return self.tamanho == 0

    def __len__(self):
        """Retorna o número de elementos no deque."""
        return self.tamanho

# Testando a implementação
deque = DequeArray(5)
deque.append(10)
deque.append(20)
deque.appendleft(5)
print(deque.popleft())  # Output: 5
print(deque.pop())      # Output: 20
print(len(deque))       # Output: 1
