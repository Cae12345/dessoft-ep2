def afundados(frota, tab):
    soma = 0
    for modelo, nav in frota.items():
        for navio in nav:
            for posi in navio:
                if tab[posi[0]][posi[1]] != 'X':
                    break
            else:
                soma += 1
    return soma