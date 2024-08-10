import os
import sys
import time
tamanho_terminal = os.get_terminal_size()
altura = tamanho_terminal.lines
largura = tamanho_terminal.columns

class construct_ui():
    def __init__(self, preencher='.',altura=altura,largura=largura):
    	self.tabuleiro = [[preencher for _ in range(largura)] for _ in range(altura)]
    def add_component(self, x, y,character):
    	if 0<= x < len(self.tabuleiro) and 0<= y <len(self.tabuleiro[0]):
    		self.tabuleiro[y][x] = character
    	else:
            print(f"Coordenadas ({x}, {y}) fora dos limites do tabuleiro.")
    def update(self):
        try:
                sys.stdout.write('\033[2J\033[H')
                sys.stdout.flush()
                for linha in self.tabuleiro:
                	linha = "".join(linha)
                	print(f"{linha}")
                	sys.stdout.write('\r')
                	sys.stdout.flush()
                #print(self.exibir_tabuleiro)
                
        except Exception as e:
            print("ERRO: ",e)
    	
tabuleiro = construct_ui(altura=altura//2,largura=largura)
tabuleiro.add_component(10,10, '$')
tabuleiro.add_component(15,10, '$')
while True:
	tabuleiro.update()
	time.sleep(0.2) 
