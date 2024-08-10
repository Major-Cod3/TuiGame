def style(d, prefixo=''):
    for chave, valor in d.items():
        if isinstance(valor, dict):
            # Chama recursivamente para dicionários aninhados
            yield from style(valor, prefixo + chave + '.')
        else:
            # Gera o valor com o prefixo acumulado
            yield f'{prefixo}{chave}("{valor}")'

