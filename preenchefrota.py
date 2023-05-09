def define_posicoes(linha, col, ori, tam):
    posi = []
    if ori == "vertical":
        for i in range(tam):
            posi.append([linha + i, col])
    else:
        for i in range(tam):
            posi.append([linha, col + i])
    return posi
    

def preenche_frota(frota, nome, linha, col, ori, tam):
    posi = define_posicoes(linha, col, ori, tam)
    if nome not in frota:
        frota[nome] = [posi]
    else:
        frota[nome].append(posi)
    return frota