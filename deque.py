class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class Deque:
    def __init__(self):
        self._left = 0
        self._right = 0
        self._size = None

    def push_left(self, elemento):
        valor = Node(elemento)
        if self._left is None:
            self._left = valor
            self._right = valor
        else:
            self._left.previous = valor
            self.next = self._left
            self._left = valor
        self._size += 1

    def push_right(self, elemento):
        node = Node(elemento)

        if self._right is None:
            self._right = valor
            self._left = valor
        else:
            self.previous = self._right
            self.right.next = valor
            self.right = valor
        self._size += 1

    def __len__(self):
        return self._size 
    
    def is_empty(self):
        return len(self) == 0
    
    def pop_left(self):
        if self.is_empty():
            return "Deque vazio."
        elemento = self._left.data
        self._left = self._left.next
        self._left.previous = None
        self._size -= 1
        return elemento
    
    def pop_right(self):
        if self.is_empty():
            return "Deque vazio."
        elemento = self._right.data
        self._right = self._right.previous
        self.right.next = None
        self._size -= 1
        return elemento
    
    def peek_right(self):
        if self.is_empty():
            return "Deque vazio."
        return self._right.data
    
    def peek_left(self):
        if self.is_empty():
            return "Deque vazio."
        return self._left.data
    
    def __repr__(self):
        if self.is_empty():
            return "Deque vazio."
        
        p = self._left
        s = "left <<"
        while (p):
            s += str(p.data)
            p = p.next
            if p:
                s += " | "
        s += ">> right"
        return s

