## Descrição do Projeto

O TuiGame é uma biblioteca Python para criar jogos interativos em um ambiente de terminal. O projeto oferece uma estrutura para a criação de tabuleiros personalizados, permitindo aos desenvolvedores adicionar elementos visuais, como títulos e cores, e interagir com os jogadores através da captura de teclas.

### Instalação

Para utilizar o TuiGame, é necessário ter o Python instalado. Além disso, as bibliotecas blessed e pyfiglet devem ser instaladas. Utilize os seguintes comandos para instalar as bibliotecas:
```python
pip install blessed pyfiglet
```

## Uso

Após a instalação, você pode importar o módulo e começar a construir seu jogo. O TuiGame permite a criação de tabuleiros e a personalização de suas cores e títulos.

### Requisitos

Python 3.x

Bibliotecas blessed e pyfiglet


Componentes do Jogo

1. **Tabuleiro**

O tabuleiro é a base do jogo, onde os elementos interativos serão apresentados. O projeto permite definir o tamanho do tabuleiro e adicionar elementos visuais, como títulos e cores de fundo.

2. **Títulos e Cores**

Você pode personalizar os títulos do tabuleiro usando a classe title, que utiliza a biblioteca pyfiglet para gerar texto estilizado.

3. **Objetos**

Os objetos são elementos que podem ser adicionados, movidos e deletados no tabuleiro.

Classes e Funções Principais

### Classe title

- A classe title é responsável por gerar um título estilizado para o jogo.

- Método __init__(self, title, font='big_money-se', justify='center'): Construtor que gera o título utilizando a fonte especificada.

- Método font_r(self): Retorna uma lista de fontes recomendadas.


### Classe TUI

- A classe TUI gerencia o tabuleiro e a interação dos objetos.

- Método __init__(self, altura, largura, x=0, y=0): Construtor que inicializa o terminal, define as dimensões do tabuleiro e chama tabuleiro_reset().

- Método tabuleiro_reset(self): Reseta o tabuleiro para suas dimensões iniciais, preenchendo-o com um fundo padrão.

- Método text_object(self, x, y, text): Exibe texto em uma posição específica do terminal.

- Método add_object(self, x, y, object, id): Adiciona um objeto ao tabuleiro na posição (x, y) com um identificador único.

- Método delete_object(self, id): Remove um objeto do tabuleiro utilizando seu identificador.

- Método move_object(self, id, new_x, new_y): Move um objeto para uma nova posição no tabuleiro.

- Método update(self): Atualiza o terminal para refletir o estado atual do tabuleiro e dos objetos.
