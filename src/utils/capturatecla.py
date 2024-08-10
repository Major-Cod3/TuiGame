import sys
import tty
import termios
import threading
import os

escape_sequences = {
    'cursor_left': b'\x1b[D',
    'cursor_up': b'\x1b[A',
    'cursor_down': b'\x1b[B',
    'cursor_right': b'\x1b[C',
    'cursor_end': b'\x1b[F',
    'cursor_home': b'\x1b[H',
    'page_up': b'\x1b[5~',
    'page_down': b'\x1b[6~'
}

def clear_screen_and_home():
    """Limpa a tela e posiciona o cursor no início."""
    sys.stdout.write('\033[2J')  # Limpa a tela
    sys.stdout.write('\033[H')   # Move o cursor para o início
    sys.stdout.write('\r')
    sys.stdout.flush()

def restore_terminal():
    """Restaura as configurações do terminal e limpa a tela."""
    sys.stdout.write('\033[0m')  # Restaura a cor do texto
    sys.stdout.flush()
    clear_screen_and_home()  # Limpa a tela e reposiciona o cursor
    sys.exit()

def getch():
    sys.stdout.write("\x1b[?1000h")
    sys.stdout.write("\x1b[0G\x1b[K")
    sys.stdout.flush()
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    escape_sequence = b''
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch == '\x1b':  # Detecta o início da sequência de escape
                escape_sequence = ch.encode()  # Inicia uma nova sequência de escape
                while True:
                    ch = sys.stdin.read(1)
                    escape_sequence += ch.encode()
                    # Verifica se a sequência de escape atual corresponde a alguma conhecida
                    if ch == 'M':
                        mouse_event = sys.stdin.read(3)
                        if mouse_event:
                            button, x, y = ord(mouse_event[0]), ord(mouse_event[1]), ord(mouse_event[2])
                            # Limpa a linha e move o cursor para o início da linha
                            sys.stdout.write("\x1b[0G\x1b[K")
                            # Imprime a nova informação
                            return 'M', button, x, y
                    for nome, valor in escape_sequences.items():
                        if escape_sequence.endswith(valor):
                            sys.stdout.write("\x1b[0G\x1b[K")
                            sys.stdout.flush()
                            return nome
                    # Se a sequência ainda não estiver completa, continue acumulando
                    if len(escape_sequence) > 1 and not any(escape_sequence.endswith(val) for val in escape_sequences.values()):
                        continue
                    break
            else:
                sys.stdout.write("\x1b[0G\x1b[K")
                sys.stdout.flush()
                return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

class KeyPressListener:
    def __init__(self):
        sys.stdout.write("\x1b[0G\x1b[K")
        sys.stdout.flush()
        self.key_pressed = None
        self.lock = threading.Lock()
        self.new_key_pressed = threading.Event()
        self.thread = threading.Thread(target=self.listen_for_keypress, daemon=True)
        self.thread.start()

    def listen_for_keypress(self):
        while True:
            key = getch()
            sys.stdout.write("\x1b[0G\x1b[K")
            sys.stdout.flush()
            
            with self.lock:
                sys.stdout.write("\x1b[0G\x1b[K")
                sys.stdout.flush()
                self.key_pressed = key
                self.new_key_pressed.set()

    def get_key(self):
        self.new_key_pressed.wait()
        with self.lock:
            key = self.key_pressed
            self.new_key_pressed.clear()
            clear_screen_and_home()  # Limpa a tela e reposiciona o cursor
            
            return key

if __name__ == "__main__":
    listener = KeyPressListener()

    try:
        while True:
            key = listener.get_key()
            if key:
                print(f"Key pressed: {repr(key)}", end='', flush=True)
    except KeyboardInterrupt:
        restore_terminal()
        print("\nPrograma encerrado.")
    finally:
        print('fui')
        restore_terminal()