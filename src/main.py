import os
import sys
from utils import color
import themes
import time
import json
import json_style
json_string = '''
{
  "tui": {
    "tema": "THEME_RED",
    "titler": "Major"
  },
  "tui2": {
    "tema": "THEME_LIGHT_2",
    "titler": "Major"
  },
  "tui3": {
    "tema": "THEME_PURPLE",
    "titler": "Major"
  }
}
'''

# Converte a string JSON para um dicionário
dados = json.loads(json_string)

class TUI:
    def __init__(self,altura, largura,x, y):
    	self.altura, self.largura = altura, largura
    	self.x = x
    	self.y = 1 if y==0 else y
    	self.themes = themes.THEME_DARK_1
    	self.tabuleiro = [[self.themes + ' ' + themes.RESET for _ in range(self.largura)] for _ in range(self.altura)]
    def tema(self,nome_tema):
    	self.themes = getattr(themes, nome_tema, None)
    	if self.themes is None:
    		raise ValueError(f"O tema '{nome_tema}' não foi encontrado.")
    	else:
    		self.tabuleiro = [[self.themes + ' ' + themes.RESET for _ in range(self.largura)] for _ in range(self.altura)]
    def titler(self, titulo):
        # Calcular a posição central para o título
        centro = (self.largura - len(titulo)) // 2
        if centro < 0:
            centro = 0
        # Garantir que o título se encaixe no tabuleiro
        if centro + len(titulo) > self.largura:
            titulo = titulo[:self.largura - centro]
        # Colocar o título na primeira linha do tabuleiro
        linha = [' '] * self.largura  # Linha em branco
        for i, t in enumerate(titulo):
            linha[centro + i] ='\033[1m' + t +'\033[0m'
        self.tabuleiro[0] = linha
    def update(self):
        for linha_index, linha in enumerate(self.tabuleiro):
            sys.stdout.write(f'\033[{self.y + linha_index};{self.x}H')  # Move o cursor para a posição da linha atual
            sys.stdout.write(''.join(linha))
            sys.stdout.write('\n')
        sys.stdout.flush()
    	

# Exemplo de uso
if __name__ == "__main__":
        tui = TUI(30,83,x=0,y=0)
        tui2 = TUI(30,83,x=0,y=30)
        tui3 = TUI(30,83,x=0,y=60)
        for style in json_style.style(dados):
        	eval(style)
        tui.update()
        tui2.update()
        tui3.update()