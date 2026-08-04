
# def melhor_opcao(capacidade_atual, itens, beneficios, pesos):
#     # encontra a melhor opcao de custo beneficio
#     achou = False

#     i = 0
#     n = len(itens)
#     while i < n: # While para remover os itens que não cabem na mochila
       
#         if i == n: # Se acabou a mochila
#             return -1

#        # Sendo um algoritmo guloso (não retiramos itens da mochila depois de colocar), 
#        # se não cabe no estado atual da mochila, não vai caber nos próximos estados da mochila
#        # logo, é possível retirar o item agora
#         if pesos[i] > capacidade_atual:
#             itens.pop(i)
#             pesos.pop(i)
#             beneficios.pop(i)
#             i-=1
#             continue

#         i+=1
        

#     melhor = 0
#     # Busca pelo melhor item no conjunto atual
#     for j in range(n-i): 
#         if beneficios[j] > beneficios[melhor]:
#             melhor = j

#     return melhor

def melhor_opcao(capacidade_atual, itens, valores, pesos, beneficios):
    # encontra a melhor opcao de custo beneficio
    achou = False

    while not achou:
       
        if len(itens) == 0: # Se acabou os itens
            return -1
        
        melhor = 0
        # Busca pelo melhor item no conjunto atual
        for i in range(len(itens)): 
            if beneficios[i] > beneficios[melhor]:
                melhor = i

        # Se cabe na mochila, achou
        if pesos[melhor] <= capacidade_atual:
            achou = True

        # Otimização
        # Se não cabe, remove da mochila e procura o próximo melhor
        else:
            itens.pop(melhor)
            pesos.pop(melhor)
            beneficios.pop(melhor)
            valores.pop(melhor)

    if achou == False:
        return -1
    else:
        return melhor

def BinGreedy(capacidade: int,
            itens: list[int],
            valores : list[int],
            pesos : list[int], 
            n : int):

    beneficios = []
    mochila = [] # contém os índices dos itens que foram escolhidos para a mochila

    # calcula o custo beneficio de cada item
    for i in range(n):
        # Verifica divisão por zero para evitar que o código quebre caso peso seja 0
        valor = valores[i]
        peso = pesos[i]
        cb = valor / peso if peso > 0 else float('inf') # sempre vai escolher um item de peso 0 primeiro
        beneficios.append(cb) # ROUND PARA DEBUG, RETIRAR DEPOIS !!!!!!!!!!!!!


    valor_total = 0 # 
    i = -1
    # enquanto houver capacidade na mochila e itens para escolher
    while capacidade > 0 and len(itens) > 0:
        i+=1

        melhor = melhor_opcao(capacidade, itens, valores, pesos, beneficios)

        # print(f"Iteração {i}")
        # print(f"    Mochila = ", mochila)
        # print(f"    Capacidade atual = ", capacidade)
        # print(f"    Itens = ", itens)
        # print(f"    Pesos = ", pesos)
        # print(f"    Beneficios = ", beneficios)
        # print(f"    Melhor = index {melhor} = Item {itens[melhor]} com beneficio {beneficios[melhor]} ()")

        # input()

        # Se não houver mais itens que caibam na mochila, encerra o loop
        if melhor == -1:
            break

        # adiciona o item na mochila
        capacidade -= pesos[melhor]
        valor_total += valores[melhor]
        mochila.append(itens[melhor])

        # remove o item da lista de itens
        itens.pop(melhor)
        beneficios.pop(melhor)
        valores.pop(melhor)
        pesos.pop(melhor)

    return valor_total, sorted(mochila)


        