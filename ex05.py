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

    def add(self, item, pos):
        """Adiciona um item em uma posição específica do deque."""
        if pos < 0 or pos > self.tamanho:
            raise IndexError("Posição inválida")

        if self.tamanho == self.capacidade:
            raise OverflowError("Deque está cheio")

        # Move os elementos da posição especificada até o final para a direita
        index = (self.inicio + pos) % self.capacidade
        # Mover elementos à direita para liberar espaço
        for i in range(self.tamanho, pos, -1):
            self.fila[(self.inicio + i) % self.capacidade] = self.fila[(self.inicio + i - 1) % self.capacidade]

        # Adiciona o novo item na posição desejada
        self.fila[index] = item
        self.tamanho += 1

    def empty(self):
        """Verifica se o deque está vazio."""
        return self.tamanho == 0

    def __len__(self):
        """Retorna o número de elementos no deque."""
        return self.tamanho

    def __str__(self):
        """Representação do deque como string."""
        items = []
        for i in range(self.tamanho):
            items.append(self.fila[(self.inicio + i) % self.capacidade])
        return f"Deque: {items}"

# Testando a implementação
deque = DequeArray(5)
deque.append(10)
deque.append(20)
deque.append(30)
print(deque)  # Deque: [10, 20, 30]

deque.add(15, 1)  # Adiciona 15 na posição 1
print(deque)  # Deque: [10, 15, 20, 30]

deque.add(5, 0)  # Adiciona 5 na posição 0
print(deque)  # Deque: [5, 10, 15, 20, 30]
