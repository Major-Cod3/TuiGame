# terminal_utils.py

import sys
import os

def clear_screen():
    tamanho_terminal = os.get_terminal_size()
    altura = tamanho_terminal.lines
    largura = tamanho_terminal.columns
    for a in range(altura):
        for l in range(largura):
            sys.stdout.write(f'\033[{a};{l}H')
            #sys.stdout.write('\033[48;5;255m \033[0m')
            sys.stdout.flush()
    sys.stdout.write(f'\033[1;0H')

def move_cursor(x, y):
    sys.stdout.write(f'\033[{y};{x}H')

def hide_cursor():
    sys.stdout.write('\033[?25l')

def show_cursor():
    sys.stdout.write('\033[?25h')

#def change_color(color_code):
#    sys.stdout.write(f'\033[48;5;{color_code}m')