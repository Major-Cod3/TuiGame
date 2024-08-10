# color_themes.py

def theme_code(text_color, background_color):
    return f"\033[38;5;{text_color}m\033[48;5;{background_color}m"

# Definindo temas
THEME_DARK_1 = theme_code(254, 235)
THEME_DARK_2 = theme_code(118, 236)
THEME_LIGHT_1 = theme_code(232, 250)
THEME_LIGHT_2 = theme_code(32, 230)
THEME_BLUE = theme_code(117, 24)
THEME_RED = theme_code(196, 124)
THEME_GREEN = theme_code(82, 22)
THEME_YELLOW = theme_code(227, 94)
THEME_PURPLE = theme_code(141, 54)
THEME_CYAN = theme_code(51, 16)

# Reset para voltar às cores padrão
RESET = "\033[0m"
# exemplo.py

