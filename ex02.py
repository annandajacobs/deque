'''
2. Suponha que você tem um deque D contendo os números (1,2,3,4,5,6,7,8) , nesta ordem. Suponha também que você
inicialmente uma fila F vazia. Apresente o código que usa SOMENTE D e F (e nenhuma outra variável) e armazena em F os elementos
de na ordem (1,2,3,4,5,6,7,8) .
'''
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
