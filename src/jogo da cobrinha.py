from main import TUI,title
import time
import random
import event

# Coordenadas iniciais do corpo da cobrinha (lista de partes do corpo)
snake_body = [(30//2, 30//2)]  # Começa com apenas a cabeça

# Direção inicial (1 = baixo, -1 = cima, 2 = direita, -2 = esquerda)
direction = 2

# Função para mudar a direção com base na entrada do usuário
def change_direction(key):
    global direction
    if key == '2' and direction != 1:
        direction = -1  # Cima
    elif key == '8' and direction != -1:
        direction = 1  # Baixo
    elif key == '4' and direction != 2:
        direction = -2  # Esquerda
    elif key == '6' and direction != -2:
        direction = 2  # Direita

# Função para atualizar a posição da cobrinha com base na direção
def move():
    global snake_body
    head_x, head_y = snake_body[-1]  # Posição da cabeça atual
    

    # Calcula a nova posição da cabeça
    if direction == 1:
        head_y += 1  # Move para baixo
    elif direction == -1:
        head_y -= 1  # Move para cima
    elif direction == 2:
        head_x += 1  # Move para a direita
    elif direction == -2:
        head_x -= 1  # Move para a esquerda

    # Controla a "teleportação" da cobrinha caso chegue ao fim do campo
    head_x = head_x % 30
    head_y = head_y % 30

    # Adiciona a nova posição da cabeça ao corpo
    snake_body.append((head_x, head_y))

    # Remove a cauda da cobrinha (exceto se for crescer)
    if not grow:
        
        
        tui.tabuleiro_reset()
        snake_body.pop(0)
        

# Função para gerar uma posição aleatória para a comida
def gerar_posicao_aleatoria():
    return (random.randint(0, 29), random.randint(0, 29))

# Inicializando TUI


# Inicializando posição da comida
posicao_comida = gerar_posicao_aleatoria()
print("\033[?25l", end="")
tui = TUI(30, 30, 20, 12)
# Adicionando a comida ao tabuleiro
tui.add_object(posicao_comida[0], posicao_comida[1], '•', id='comida')
title('Snake',font='isometric2')
grow = False  # Indica se a cobrinha deve crescer

while True:
    tui.tabuleiro_reset()
    # Obtendo a tecla pressionada
    key = event.get_pressed_key()
    if key in ['2', '8', '4', '6']:
        change_direction(key)

    # Movendo a cobrinha
    move()
    if snake_body[-1] == posicao_comida:
        grow = True  # A cobrinha deve crescer no próximo movimento
        posicao_comida = gerar_posicao_aleatoria()
        tui.add_object(posicao_comida[0], posicao_comida[1], '•', id='comida')
    else:
        grow = False
    # Atualizando as posições da cobrinha na tela
    for i, (x, y) in enumerate(snake_body):
        if i== len(snake_body) -1:
        	tui.add_object(x, y, '\033[38;5;1m\033[48;5;1m#\033[0m', id=f'snake_part_{i}')
        else:
        	tui.add_object(x, y, '\033[38;5;10m\033[48;5;10m#\033[0m', id=f'snake_part_{i}')
    # Checando se a cobrinha comeu a comida
    

    # Atualizando a tela
    tui.update()

    # Pausa para desacelerar o movimento
    time.sleep(1 /10)
    