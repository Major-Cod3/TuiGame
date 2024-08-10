colors_ansi = {
    "AliceBlue": "153",  # Aproximado
    "AntiqueWhite": "222",  # Aproximado
    "Aqua": "14",  # Aproximado
    "Aquamarine": "81",  # Aproximado
    "Azure": "153",  # Aproximado
    "Beige": "230",  # Aproximado
    "Bisque": "223",  # Aproximado
    "Black": "0",
    "BlanchedAlmond": "229",  # Aproximado
    "Blue": "4",
    "Red": "1",
    "BlueViolet": "56",
    "Brown": "94",
    "BurlyWood": "180",
    "CadetBlue": "86",
    "Chartreuse": "118",
    "Chocolate": "130",
    "Coral": "209",
    "CornflowerBlue": "66",
    "Cornsilk": "230",
    "Crimson": "88",
    "Cyan": "14",
    "DarkBlue": "17",
    "DarkCyan": "18",
    "DarkGoldenRod": "136",
    "DarkGray": "236",
    "DarkGreen": "22",
    "DarkKhaki": "143",
    "DarkMagenta": "55",
    "DarkOliveGreen": "102",
    "DarkOrange": "208",
    "DarkOrchid": "98",
    "DarkRed": "52",
    "DarkSalmon": "204",
    "DarkSeaGreen": "59",
    "DarkSlateBlue": "17",
    "DarkSlateGray": "235",
    "DarkTurquoise": "30",
    "DarkViolet": "54",
    "DeepPink": "198",
    "DeepSkyBlue": "39",
    "DimGray": "59",
    "DodgerBlue": "39",
    "FireBrick": "124",
    "FloralWhite": "231",
    "ForestGreen": "22",
    "Fuchsia": "13",
    "Gainsboro": "253",
    "GhostWhite": "255",
    "Gold": "220",
    "GoldenRod": "136",
    "Gray": "240",
    "Green": "28",
    "GreenYellow": "118",
    "HoneyDew": "157",
    "HotPink": "213",
    "IndianRed": "88",
    "Indigo": "18",
    "Ivory": "230",
    "Khaki": "143",
    "Lavender": "189",
    "LavenderBlush": "232",
    "LawnGreen": "118",
    "LightBlue": "153",
    "LightCoral": "188",
    "LightCyan": "159",
    "LightGoldenRodYellow": "227",
    "LightGray": "253",
    "LightGreen": "118",
    "LightPink": "219",
    "LightSalmon": "209",
    "LightSeaGreen": "37",
    "LightSkyBlue": "117",
    "LightSlateGray": "251",
    "LightSteelBlue": "145",
    "LightYellow": "229",
    "Lime": "10",
    "LimeGreen": "77",
    "Linen": "230",
    "Magenta": "13",
    "Maroon": "52"
}

class setComponentColor():

    def __init__(self, color):
        self.cor = ''
        
        if isinstance(color, tuple) and len(color) == 3:
            # Converte valores RGB para o código de cor ANSI de 256 cores.
            ansi = 16 + 36 * (color[0] // 51) + 6 * (color[1] // 51) + (color[2] // 51)
            self.cor = f'\033[38;5;{ansi}m'
        elif isinstance(color, str):
            color = color.strip()
            if color in colors_ansi:
                self.cor = f'\033[38;5;{colors_ansi[color]}m'
            elif color.startswith('#'):
                # Converte um código hexadecimal para valores ANSI.
                hex_color = color.lstrip('#')
                if len(hex_color) == 6:
                    try:
                        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                        ansi = 16 + 36 * (r // 51) + 6 * (g // 51) + (b // 51)
                        self.cor = f'\033[38;5;{ansi}m'
                    except ValueError:
                        raise ValueError("Código hexadecimal inválido.")
                else:
                    raise ValueError("Código hexadecimal deve ter 6 caracteres.")
            else:
                raise ValueError("Cor inválida.")

    def __str__(self):
        return f'{self.cor}'

    def reset_color(self):
        """Reseta a cor para o padrão."""
        self.cor = '\033[0m'

class bgColor():

    def __init__(self, color):
        self.cor = ''
        if isinstance(color, tuple) and len(color) == 3:
            # Converte valores RGB para o código de cor ANSI de 256 cores.
            ansi = 16 + 36 * (color[0] // 51) + 6 * (color[1] // 51) + (color[2] // 51)
            self.cor = f'\033[48;5;{ansi}m'
        elif isinstance(color, str):
            color = color.strip()
            if color in colors_ansi:
                self.cor = f'\033[48;5;{colors_ansi[color]}m'
            elif color.startswith('#'):
                # Converte um código hexadecimal para valores ANSI.
                hex_color = color.lstrip('#')
                if len(hex_color) == 6:
                    try:
                        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                        ansi = 16 + 36 * (r // 51) + 6 * (g // 51) + (b // 51)
                        self.cor = f'\033[48;5;{ansi}m'
                    except ValueError:
                        raise ValueError("Código hexadecimal inválido.")
                else:
                    raise ValueError("Código hexadecimal deve ter 6 caracteres.")
            else:
                raise ValueError("Cor inválida.")

    def __str__(self):
        return f'{self.cor}'

    def reset_color(self):
        """Reseta a cor para o padrão."""
        self.cor = '\033[0m'
        
