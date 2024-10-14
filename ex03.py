'''
3. João tem 4 vacas que ele deseja levar para o outro lado de um ponto, mas somente uma canga que permite colocar duas vagas, lado
a lado, amarradas na canga. A canga é muito pesada pela ele carregar pela ponte, mas ele consegue prender (e soltar) as vacas na canga a qualquer momento sem gastar muito tempo (tempo 0). Das suas vacas:
    - Malhada pode atravessar a ponte em 2 minutos
    - Estrelinha pode atravessar em 4 minutos
    - Celeste pode atravessar em 10 minutos
    - Pintada pode atravessar em 20 minutos.
Claro, quando duas vagas são unidas a canga, elas se andam na velocidade da vaca mais lenta. Descreva como João pode levar todas as vacas pela ponte em 34 minutos ou menos.
canga = peça de madeira usada para atrelar bois a carroça ou arado, para que andem no mesmo compasso; jugo.
'''
from collections import deque

# Inicializa o deque com as vacas e seus tempos de travessia
vacas = deque([
    ("Malhada", 2),    # Tempo de travessia 2 minutos
    ("Estrelinha", 4), # Tempo de travessia 4 minutos
    ("Celeste", 10),   # Tempo de travessia 10 minutos
    ("Pintada", 20)    # Tempo de travessia 20 minutos
])

# Inicializa o tempo total
tempo_total = 0

# Lista para registrar as travessias
log = []

# Passo 1: Malhada e Estrelinha atravessam primeiro
vaca1 = vacas.popleft()  # Malhada
vaca2 = vacas.popleft()  # Estrelinha
tempo_total += vaca2[1]  # Tempo é ditado pela vaca mais lenta (Estrelinha)
log.append(f"{vaca1[0]} e {vaca2[0]} atravessam. Tempo: {vaca2[1]} min")

# Malhada volta com a canga
vacas.appendleft(vaca1)  # Coloca Malhada de volta no início
tempo_total += vaca1[1]  # Malhada volta sozinha
log.append(f"{vaca1[0]} volta. Tempo: {vaca1[1]} min")

# Passo 2: Celeste e Pintada atravessam
vaca3 = vacas.pop()      # Pintada
vaca4 = vacas.pop()      # Celeste
tempo_total += vaca3[1]  # Tempo é ditado pela vaca mais lenta (Pintada)
log.append(f"{vaca4[0]} e {vaca3[0]} atravessam. Tempo: {vaca3[1]} min")

# Estrelinha volta com a canga
vacas.appendleft(vaca2)  # Coloca Estrelinha de volta no início
tempo_total += vaca2[1]  # Estrelinha volta sozinha
log.append(f"{vaca2[0]} volta. Tempo: {vaca2[1]} min")

# Passo 3: Malhada e Estrelinha atravessam novamente
vaca1 = vacas.popleft()  # Malhada
vaca2 = vacas.popleft()  # Estrelinha
tempo_total += vaca2[1]  # Tempo é ditado por Estrelinha
log.append(f"{vaca1[0]} e {vaca2[0]} atravessam. Tempo: {vaca2[1]} min")

# Exibe o tempo total e o registro das travessias
print(f"Tempo total: {tempo_total} minutos\n")
print("Registro das travessias:")
for evento in log:
    print(evento)
