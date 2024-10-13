# TuiGame

O pacote **TuiGame** (Terminal User Interface Game) fornece uma estrutura para a criação de jogos simples em um ambiente de terminal. Ele permite a manipulação de objetos em um tabuleiro, com suporte para cores e captura de eventos do teclado, facilitando a implementação de mini jogos.

[Documentação Completa](https://tuigame.readthedocs.io/en/latest/)

## Módulos

1. **tui.py**

   Este é o módulo principal que define a classe `TUI`, permitindo a criação e movimentação de objetos no tabuleiro.

   ### Classes e Métodos

   - `title`: Classe para exibir títulos estilizados.
   - `TUI`: Classe que gerencia a interface do terminal.
   - `add_object(x, y, object, id)`: Adiciona um objeto na posição especificada.
   - `move_object(id, new_x, new_y)`: Move um objeto para uma nova posição.
   - `update()`: Atualiza a interface do terminal para refletir as mudanças.

2. **color.py**

   Este módulo contém funções e classes que permitem aplicar cores aos objetos exibidos no terminal.

3. **event.py**

Este módulo é responsável pela captura de eventos do teclado, permitindo interações do usuário com a interface.