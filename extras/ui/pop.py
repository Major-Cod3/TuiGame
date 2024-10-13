import sys
tabuleiro = [['\033[48;5;255m \033[0m' for _ in range(50)] for _ in range(20)]
y =10
num_linhas = len(tabuleiro)
num_colunas = len(tabuleiro[0])

# Preencher a borda superior e inferior com '#'
for i in range(num_colunas):
    tabuleiro[0][i] = '\033[48;5;33m \033[0m'
    tabuleiro[num_linhas - 1][i] = '\033[48;5;33m \033[0m'

# Preencher a borda esquerda e direita com '#'
for i in range(1, num_linhas - 1):
    tabuleiro[i][0] = '\033[48;5;33m \033[0m'
    tabuleiro[i][num_colunas - 1] = '\033[48;5;33m \033[0m'
for i, linha in enumerate(tabuleiro):
    sys.stdout.write(f"\033[{y};10H")
    y +=1
    print(''.join(linha))