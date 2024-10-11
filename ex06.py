from collections import deque

def is_palindrome(s):
    # Limpa a string, removendo espaços e caracteres especiais, e converte para minúsculas
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Inicializa o deque
    d = deque(cleaned)
    
    # Verifica se a string é um palíndromo
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
            
    return True

# Testando a função
test_strings = [
    "A man, a plan, a canal, Panama!",
    "Racecar",
    "Hello",
    "Was it a car or a cat I saw?",
    "No 'x' in Nixon"
]

for test in test_strings:
    result = is_palindrome(test)
    print(f'"{test}" is a palindrome: {result}')
