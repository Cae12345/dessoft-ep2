def define_posicoes(linha, col, ori, tam):
    nova_lista = []
    if ori == 'vertical':
        for i in range(tam):
            nova_lista.append([linha + i, col])
    elif ori == 'horizontal':
        for i in range(tam):
            nova_lista.append([linha, col + i])
    return nova_lista

def preenche_frota(frota, nome, linha, col, ori, tam):

    posicao = define_posicoes(linha, col, ori, tam)
    if nome not in frota:
        frota[nome] = list()
    frota[nome].extend([posicao])
    return frota
def posicao_valida(frota, linha, col, ori, tam):
    novas_posicoes = define_posicoes(linha, col, ori, tam)
    posi_cheio = {}
    for nome_navio in frota:
        navios = frota[nome_navio]
        for i in range(len(navios)):
            navio = navios[i]
            for j in range(len(navio)):
                posicao = navio[j]
                posi_cheio[(posicao[0], posicao[1])] = True
    for i in range(len(novas_posicoes)):
        posicao = novas_posicoes[i]
        if posicao[0] < 0 or posicao[0] >= 10 or posicao[1] < 0 or posicao[1] >= 10:
            return False
        if (posicao[0], posicao[1]) in posi_cheio:
            return False
    return True

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
tam = 4
nome = 'porta-aviões'
while True:
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    ori = int(input('[1] Vertical [2] Horizontal >'))
    if ori == 1:
        ori = 'vertical'
    else:
        ori = 'horizontal'
    if posicao_valida(frota, linha, coluna, ori, tam) == True:
        preenche_frota(frota, nome, linha, coluna, ori, tam)

        break

    else:
        print('Esta posição não está válida!')
        print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
i = 0
while i < 2:

    print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')
    tam = 3
    nome = 'navio-tanque'
    while True:
        linha = int(input('Linha: '))
        col = int(input('Coluna: '))
        ori = int(input('[1] Vertical [2] Horizontal >'))
        if ori == 1:
            ori = 'vertical'
        else:
            ori = 'horizontal'
        if posicao_valida(frota, linha, col, ori, tam) == True:
            preenche_frota(frota, nome, linha, col, ori, tam)

            i+=1
            break

        else:
            print('Esta posição não está válida!')
            print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')

z = 0
while z < 3:
    print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')
    tam = 2
    nome = 'contratorpedeiro'
    while True:
        linha = int(input('Linha: '))
        col = int(input('Coluna: '))
        ori = int(input('[1] Vertical [2] Horizontal >'))
        if ori == 1:
            ori = 'vertical'
        else:
            ori = 'horizontal'
        if posicao_valida(frota, linha, col, ori, tam) == True:
            preenche_frota(frota, nome, linha, col, ori, tam)

            z+=1

            break

        else:
            print('Esta posição não está válida!')
            print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')


l = 0

while l < 4:

    print('Insira as informações referentes ao navio submarino que possui tamanho 1')
    tamanho = 1
    nome = 'submarino'
    while True:
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if posicao_valida(frota, linha, coluna, ori, tamanho) == True:
            preenche_frota(frota, nome, linha, coluna, ori, tamanho)

            l+=1

            break

        else:
            print('Esta posição não está válida!')
            print('Insira as informações referentes ao navio submarino que possui tamanho 1')



print(frota)