from collections import deque

# Inicializa o deque D com os elementos
D = deque([1, 2, 3, 4, 5, 6, 7, 8])

# Inicializa a fila F vazia
F = deque()

# Transfere os elementos de D para F mantendo a ordem
while D:
    # Remove o primeiro elemento de D e coloca no final de F
    F.append(D.popleft())

# F agora contém os elementos na ordem (1, 2, 3, 4, 5, 6, 7, 8)
print(list(F))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
