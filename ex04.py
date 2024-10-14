'''
4. Descreva como implementar um deque através da utilização de duas pilhas. Qual seria o tempo de execução dos métodos?
'''
class DequeWithStacks:
    def __init__(self):
        # Inicializa as pilhas
        self.pilha_entrada = []  # Usada para adicionar no final
        self.pilha_saida = []    # Usada para remover do início

    def append(self, item):
        """Adiciona um item no final do deque."""
        self.pilha_entrada.append(item)

    def appendleft(self, item):
        """Adiciona um item no início do deque."""
        if not self.pilha_saida:
            # Se a pilha de saída estiver vazia, movemos todos os elementos da pilha de entrada
            while self.pilha_entrada:
                self.pilha_saida.append(self.pilha_entrada.pop())
        self.pilha_saida.append(item)

    def pop(self):
        """Remove e retorna o item do final do deque."""
        if not self.pilha_entrada:
            # Se a pilha de entrada estiver vazia, movemos todos os elementos da pilha de saída
            while self.pilha_saida:
                self.pilha_entrada.append(self.pilha_saida.pop())
        if self.pilha_entrada:
            return self.pilha_entrada.pop()
        else:
            raise IndexError("pop from an empty deque")

    def popleft(self):
        """Remove e retorna o item do início do deque."""
        if not self.pilha_saida:
            # Se a pilha de saída estiver vazia, movemos todos os elementos da pilha de entrada
            while self.pilha_entrada:
                self.pilha_saida.append(self.pilha_entrada.pop())
        if self.pilha_saida:
            return self.pilha_saida.pop()
        else:
            raise IndexError("popleft from an empty deque")

    def __len__(self):
        """Retorna o número de elementos no deque."""
        return len(self.pilha_entrada) + len(self.pilha_saida)

# Testando a implementação
deque = DequeWithStacks()
deque.append(1)
deque.append(2)
deque.appendleft(0)
print(deque.popleft())  # Output: 0
print(deque.pop())      # Output: 2
print(deque.popleft())  # Output: 1
