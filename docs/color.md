# Módulo `color`

O módulo `color` do **TuiGame** permite a aplicação de cores em textos e no plano de fundo do terminal, utilizando códigos ANSI de 256 cores. Ele também suporta cores personalizadas, tanto em formato RGB quanto hexadecimal, tornando mais simples a customização da interface dos jogos no terminal.

## Mapeamento de Cores ANSI

O dicionário `colors_ansi` contém um mapeamento de nomes de cores comuns para seus respectivos códigos ANSI. Caso uma cor não esteja no dicionário, é possível utilizar códigos hexadecimais ou valores RGB para definir cores personalizadas.

## Classes

### Classe `TextColor`

A classe `TextColor` é usada para aplicar uma cor ao texto exibido no terminal. Ela suporta a definição de cores por nome (usando o dicionário `colors_ansi`), por código hexadecimal ou valores RGB.

#### Métodos

- **`__init__(self, color)`**  
  Construtor que aceita como entrada:
  - Uma `string` com o nome da cor (por exemplo, `"Red"`, `"Blue"`), conforme mapeado em `colors_ansi`.
  - Um código hexadecimal de 6 caracteres (por exemplo, `#FF0000` para vermelho).
  - Uma tupla com valores RGB (por exemplo, `(255, 0, 0)` para vermelho).

  Se o nome da cor, código hexadecimal ou tupla RGB for válido, a cor será aplicada ao texto.

- **`__str__(self)`**  
  Retorna a string correspondente ao código ANSI da cor aplicada. Pode ser utilizado diretamente em uma instrução `print` para alterar a cor do texto.

- **`reset_color(self)`**  
  Método que reseta a cor do texto para o padrão do terminal.

#### Exemplo de Uso:

```python
from color import TextColor

# Define a cor do texto usando um nome de cor
text_color = TextColor("Red")
print(f"{text_color}Este texto será vermelho.")
```
## tabela de cores:


| AliceBlue | 153 |
	------------| AntiqueWhite | 222 |
	------------| Aqua | 14 |
	------------| Aquamarine | 81 |
	------------| Azure | 153 |
	------------| Beige | 230 |
	------------| Bisque | 223 |
	------------| Black | 0 |
	------------| BlanchedAlmond | 229 |
	------------| Blue | 4 |
	------------| Red | 1 |
	------------| BlueViolet | 56 |
	------------| Brown | 94 |
	------------| BurlyWood | 180 |
	------------| CadetBlue | 86 |
	------------| Chartreuse | 118 |
	------------| Chocolate | 130 |
	------------| Coral | 209 |
	------------| CornflowerBlue | 66 |
	------------| Cornsilk | 230 |
	------------| Crimson | 88 |
	------------| Cyan | 14 |
	------------| DarkBlue | 17 |
	------------| DarkCyan | 18 |
	------------| DarkGoldenRod | 136 |
	------------| DarkGray | 236 |
	------------| DarkGreen | 22 |
	------------| DarkKhaki | 143 |
	------------| DarkMagenta | 55 |
	------------| DarkOliveGreen | 102 |
	------------| DarkOrange | 208 |
	------------| DarkOrchid | 98 |
	------------| DarkRed | 52 |
	------------| DarkSalmon | 204 |
	------------| DarkSeaGreen | 59 |
	------------| DarkSlateBlue | 17 |
	------------| DarkSlateGray | 235 |
	------------| DarkTurquoise | 30 |
	------------| DarkViolet | 54 |
	------------| DeepPink | 198 |
	------------| DeepSkyBlue | 39 |
	------------| DimGray | 59 |
	------------| DodgerBlue | 39 |
	------------| FireBrick | 124 |
	------------| FloralWhite | 231 |
	------------| ForestGreen | 22 |
	------------| Fuchsia | 13 |
	------------| Gainsboro | 253 |
	------------| GhostWhite | 255 |
	------------| Gold | 220 |
	------------| GoldenRod | 136 |
	------------| Gray | 240 |
	------------| Green | 28 |
	------------| GreenYellow | 118 |
	------------| HoneyDew | 157 |
	------------| HotPink | 213 |
	------------| IndianRed | 88 |
	------------| Indigo | 18 |
	------------| Ivory | 230 |
	------------| Khaki | 143 |
	------------| Lavender | 189 |
	------------| LavenderBlush | 232 |
	------------| LawnGreen | 118 |
	------------| LightBlue | 153 |
	------------| LightCoral | 188 |
	------------| LightCyan | 159 |
	------------| LightGoldenRodYellow | 227 |
	------------| LightGray | 253 |
	------------| LightGreen | 118 |
	------------| LightPink | 219 |
	------------| LightSalmon | 209 |
	------------| LightSeaGreen | 37 |
	------------| LightSkyBlue | 117 |
	------------| LightSlateGray | 251 |
	------------| LightSteelBlue | 145 |
	------------| LightYellow | 229 |
	------------| Lime | 10 |
	------------| LimeGreen | 77 |
	------------| Linen | 230 |
	------------| Magenta | 13 |
	------------| Maroon | 52 |
	------------