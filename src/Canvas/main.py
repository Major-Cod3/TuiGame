# Definindo o raio do círculo
r = int(input('raio: '))

matriz = r+r +1
# Criação de um tabuleiro 50x50
tabuleiro = [[' ' for _ in range(matriz)] for _ in range(matriz)]

# Definindo o centro do círculo
y_c = len(tabuleiro) // 2  # Centro do tabuleiro (25)
x_c = len(tabuleiro[0]) // 2  # Centro do tabuleiro (25)


# Verificação para cada ponto no tabuleiro
for y in range(len(tabuleiro)):
    for x in range(len(tabuleiro[y])):
        if ( (x - x_c)**2 + (y - y_c)**2 <= r**2 ):
            tabuleiro[y][x] = '\033[48;5;236m \033[0m'  # Corrigido para tabuleiro[y][x]

# Impressão do tabuleiro
for linha in tabuleiro:
    print(''.join(linha))