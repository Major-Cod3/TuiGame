import sys
import time
import os

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora você pode importar o módulo
from utils.terminal_utils import move_cursor, hide_cursor, show_cursor
from utils.color import setComponentColor

progress_styles = {
    "blocos_cheios": ["█", "░"],
    "hashes": ["#" ,"-"],
    "blocos_menor": ["█", "▓"],
    "quadrados": ["■", "□"],
    "blocos_pontilhados": ["█", "▒"],
    "blocos_finos": ["█", "░"],
    "arobases": ["@", "%"]
}
class ProgressBar(): 
    def __init__(self, iteration, total, x, y, prefix='', length=50,style='quadrados', print_end="\r"):
        move_cursor(x,y)
        hide_cursor()
        self.cor = setComponentColor("LavenderBlush")
        add_styles = progress_styles.get(style, ["■", "□"])
        self.update(iteration, total, x, y, prefix, length, print_end)
        
    def update(self, iteration, total, x, y, prefix='', length=50, print_end="\r"):
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = add_styles[0] * filled_length + add_styles[1] * (length - filled_length)
        sys.stdout.write(f'{prefix} |{self.cor}{bar}| {percent}%')
        sys.stdout.flush()
        if iteration == total:
            sys.stdout.write(print_end)
            sys.stdout.flush()
            show_cursor()
        def color(self, cor):
            self.cor = setComponentColor(cor)
# Simulação de progresso
for i in range(101):
    time.sleep(0.1)
    ProgressBar(i, 100, prefix='Progresso', style="quadrados",x=1,y=1,length=20)