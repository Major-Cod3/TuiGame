import os



def marcar_bordas(tabuleiro):
    altura = len(tabuleiro)
    largura = len(tabuleiro[0]) if altura > 0 else 0
    
    # Marcar a primeira e a última linha
    for j in range(largura):
        tabuleiro[0][j] = '\033[35m▬\033[0m'
        tabuleiro[altura-1][j] = '\033[35m▬\033[0m'
        

    # Marcar a primeira e a última coluna
    for i in range(altura):
        tabuleiro[i][0] = '\033[35m▮\033[0m'
        tabuleiro[i][largura-1] = '\033[35m▮\033[0m'
        tabuleiro[i][l//2+10] = '\033[35m▮\033[0m'
    


tamanho_terminal = os.get_terminal_size()
a = tamanho_terminal.lines
l = tamanho_terminal.columns

tabuleiro = [[' ' for _ in range(l)] for _ in range(a//2)]

marcar_bordas(tabuleiro)

for linha in tabuleiro:
    print(''.join(linha))

if any(all(c == ' ' for c in linha) for linha in tabuleiro):
    print("major")