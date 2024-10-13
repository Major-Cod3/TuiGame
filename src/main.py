import sys
import os
import time
from blessed import Terminal
import pyfiglet

class title:
	def __init__(self,title,font='big_money-se',justify='center'):
		texto = pyfiglet.figlet_format(title,font=font,justify=justify)
		print(texto)
	def font_r(self):
		fonte_Recommended=['3d-ascii','banner3-D','banner3','banner4','ansi_shadow','isometric2', 'isometric3', 'isometric4','pyramid','diet_cola','clr7x10','chiseled']
		return fonte_Recommended

class TUI:
    def __init__(self,altura, largura,x=0,y=0):
    	self.x,self.y = x,y
    	self.objects = {}
    	self.buffer = ""
    	self.term = Terminal()
    	self.altura, self.largura = altura, largura
    	self.tabuleiro_reset()
    def tabuleiro_reset(self):
    	self.tabuleiro = [['\033[48;5;24m \033[0m' for _ in range(self.largura)] for _ in range(self.altura)]
    
    def add_object(self,x,y,object,id):
    	if 0 <= y < len(self.tabuleiro) and 0 <= x < len(self.tabuleiro[1]):
    		self.objects[str(id)] = (y,x,object)
    			
    	else:
    		raise IndexError("Erro: A posição ultrapassou o tamanho do tabuleiro.")
    #Função para deleta objetos
    def delete_object(self, id):
        if id in self.objects:
            del self.objects[id]
        else:
            raise KeyError("Erro: Objeto não encontrado.")
    def move_object(self, id, new_x, new_y):
    	if id in self.objects:
    		old_y, old_x, _ = self.objects[id]
    		self.tabuleiro[old_y][old_x] = '\033[48;5;24m \033[0m'
    		if 0 <= new_y < len(self.tabuleiro) and 0 <= new_x < len(self.tabuleiro[1]):
    		      	_, _, object = self.objects[id]
    		      	self.objects[id] = (new_y, new_x, object)
    		      	self.tabuleiro[new_y][new_x] = object
    		      	
    		else:
    			raise IndexError("Erro: A posição ultrapassou o tamanho do tabuleiro.")
    	else:
    		raise KeyError("Erro: Objeto não encontrado.")
    #Função que atualiza no terminal
    def update(self):
        self.buffer = ""  # Limpa o buffer antes de cada atualização
        for chave in self.objects.keys():
            self.tabuleiro[self.objects[chave][0]][self.objects[chave][1]] = self.objects[chave][2]

        for linha_index, linha in enumerate(self.tabuleiro):
            self.buffer += self.term.move_xy(self.x, self.y + linha_index) + ''.join(linha) + '\n'
        sys.stdout.write(self.buffer)
        sys.stdout.flush()
        

# Exemplo de uso
if __name__ == "__main__":
        tui = TUI(20,20,x=30,y=16)
        y = 0
        tui.add_object(1,y,'o',id='o')
        title('teste',font='isometric2')
        time.sleep(0.5)
        while True:
        	tui.move_object('o',5,y)
        	tui.update()
        	if y ==19:
        		y=0
        	y = y +1
        	time.sleep(1/15)

