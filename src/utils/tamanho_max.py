import os
import sys
import time
from capturatecla import KeyPressListener
import capturatecla

# Configurações iniciais
tamanho_tabuleiro = 25
tabuleiro = [['.' for _ in range(tamanho_tabuleiro)] for _ in range(tamanho_tabuleiro)]
x, y = 0, 0  # Posição inicial do jogador

def exibir_tabuleiro(tabuleiro):
    os.system('cls' if os.name == 'nt' else 'clear')
    # Imprime o tabuleiro
    for linha in tabuleiro:
        linha = " ".join(linha)
        print(f"{linha}")
        sys.stdout.write('\r')
        sys.stdout.flush()
    print()  # Adiciona uma linha em branco no final

def mover_jogador(tabuleiro, x, y, direcao):
    tabuleiro[x][y] = '.'
    if direcao == '8':
        if x + 1 < tamanho_tabuleiro:
            x += 1
    elif direcao == '2':
        if x - 1 >= 0:
            x -= 1
    elif direcao == '4':
        if y - 1 >= 0:
            y -= 1
    elif direcao == '6':
        if y + 1 < tamanho_tabuleiro:
            y += 1
    tabuleiro[x][y] = '\033[91mX\033[0m'
    return x, y

# Cria uma instância do KeyPressListener
listener = KeyPressListener()

while True:
    key = listener.get_key()
    
    if key:
        #if key in ['2', '8', '4', '6']:  # As teclas válidas para movimento
        x, y = mover_jogador(tabuleiro, x, y, key)
        exibir_tabuleiro(tabuleiro)
        time.sleep(0.1) 
    if key == 'q':
    	capturatecla.restore_terminal()  
    	
    	