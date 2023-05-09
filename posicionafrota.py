def posiciona_frota(frota):
    tab = [[0]*10 for _ in range(10)]
    for nav, posi in frota.items():
        for posicao in posi:
            for x, y in posicao:
                tab[x][y] = 1
    return tab