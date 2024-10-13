from blessed import Terminal
import threading
import queue

# Inicializa o terminal
term = Terminal()

# Cria uma fila para armazenar as teclas pressionadas
key_queue = queue.Queue()

def get_key():
    with term.cbreak():
        while True:
            key = term.inkey()
            if key:
                key_queue.put(key)  # Coloca a tecla pressionada na fila

def start_key_capture():
    key_thread = threading.Thread(target=get_key)
    key_thread.daemon = True  # Torna a thread um daemon
    key_thread.start()

# Inicia a captura de teclas automaticamente ao importar o módulo
start_key_capture()

# Função para obter teclas pressionadas
def get_pressed_key():
    try:
        return key_queue.get_nowait()  # Retorna a tecla pressionada ou lança uma exceção se a fila estiver vazia
    except queue.Empty:
        return None  # Retorna None se não houver teclas pressionadas