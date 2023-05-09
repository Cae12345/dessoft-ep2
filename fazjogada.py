def faz_jogada(tab, linha, col):
    if tab[linha][col] == 1:
        tab[linha][col] = "X"
    else:
        tab[linha][col] = "-"
    return tab