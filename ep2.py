def define_posicoes(linha,col,ori,tam):
    posi = []
    for i in range(tam):
        if ori == 'vertical':
            posi.append([linha+i,col])
        if ori == 'horizontal':
            posi.append([linha,col+i])
    return posi