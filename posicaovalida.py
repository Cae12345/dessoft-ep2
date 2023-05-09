def define_posicoes(linha,col,ori,tam):
    posi = []
    for i in range(tam):
        if ori == 'vertical':
            posi.append([linha+i,col])
        if ori == 'horizontal':
            posi.append([linha,col+i])
    return posi

def posicao_valida(frota, linha, col, ori, tam):
    posi = define_posicoes(linha, col, ori, tam)
    for posicao in posi:
        if posicao[0] > 9 or posicao[1] > 9:
            return False
        for navio in frota.values():
            for posicoes_navio in navio:
                if posicao in posicoes_navio:
                    return False
    return True