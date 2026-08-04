

def FB(capacidade: int, itens: list[int], valores : list[int], pesos : list[int], n : int):

    # Testar todas as combinações possíveis de itens para encontrar a melhor solução
    # Fixa um item, adiciona-o à mochila e testa todas as combinações possíveis dos itens restantes
    # Salva a melhor solução encontrada até o momento

    """
    Faz todas as 2^n combinações possíveis de itens
    Para isso, cada valor de i representa uma combinação diferente de itens, e cada bit do valor de i representa se o item correspondente está incluído na mochila ou não
    Então se o item está na mochila, contabiliza o peso e o valor do item, depois verifica se é válido e se é melhor que a melhor solução encontrada até o momento
    """


    melhor_valor = 0
    melhor_mochila = []

    # Testa todas as combinações, cada valor de i representa uma combinação diferente de itens)
    for i in range(2**n):
        mochila_atual = []
        peso_atual = 0
        valor_atual = 0

        # Verifica quais itens estão incluídos na combinação atual
        for j in range(n):
            if (i >> j) & 1: # Move os bits do i para direita em j posições e verifica se o bit menos significativo é 1
                mochila_atual.append(itens[j]) # Adiciona o item à combinação atual
                peso_atual += pesos[j] # Contabiliza o peso
                valor_atual += valores[j] # Contabiliza o valor

        # Verifica se a combinação atual é válida e se é melhor que a melhor encontrada até agora
        if peso_atual <= capacidade and valor_atual > melhor_valor:
            melhor_valor = valor_atual
            melhor_mochila = mochila_atual

    return melhor_valor, melhor_mochila