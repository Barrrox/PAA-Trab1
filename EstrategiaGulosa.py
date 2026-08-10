
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

# def melhor_opcao(capacidade_atual, itens : list, valores, pesos, beneficios):
#     # encontra a melhor opcao de custo beneficio
#     achou = False

#     while not achou:
       
#         if len(itens) == 0: # Se acabou os itens
#             return -1
        
#         melhor = 0
#         # Busca pelo melhor item no conjunto atual
#         for i in range(len(itens)): 
#             if beneficios[i] > beneficios[melhor]:
#                 melhor = i

#         # Se cabe na mochila, achou
#         if pesos[melhor] <= capacidade_atual:
#             achou = True

#         # Otimização
#         # Se não cabe, remove da mochila e procura o próximo melhor
#         else:
#             itens.pop(melhor)
#             pesos.pop(melhor)
#             beneficios.pop(melhor)
#             valores.pop(melhor)

#     if achou == False:
#         return -1
#     else:
#         return melhor

# def BinGreedy2(capacidade: int,
#             itens: list[int],
#             valores : list[int],
#             pesos : list[int], 
#             n : int):

#     beneficios = []
#     mochila = [] # contém os índices dos itens que foram escolhidos para a mochila

#     # calcula o custo beneficio de cada item
#     for i in range(n):
#         # Verifica divisão por zero para evitar que o código quebre caso peso seja 0
#         valor = valores[i]
#         peso = pesos[i]
#         cb = valor / peso if peso > 0 else float('inf') # sempre vai escolher um item de peso 0 primeiro
#         beneficios.append(cb) # ROUND PARA DEBUG, RETIRAR DEPOIS !!!!!!!!!!!!!


#     valor_total = 0 # 
#     i = -1
#     # enquanto houver capacidade na mochila e itens para escolher
#     while capacidade > 0 and len(itens) > 0:
#         i+=1

#         melhor = melhor_opcao(capacidade, itens, valores, pesos, beneficios)

#         # print(f"Iteração {i}")
#         # print(f"    Mochila = ", mochila)
#         # print(f"    Capacidade atual = ", capacidade)
#         # print(f"    Itens = ", itens)
#         # print(f"    Pesos = ", pesos)
#         # print(f"    Beneficios = ", beneficios)
#         # print(f"    Melhor = index {melhor} = Item {itens[melhor]} com beneficio {beneficios[melhor]} ()")

#         # input()

#         # Se não houver mais itens que caibam na mochila, encerra o loop
#         if melhor == -1:
#             break

#         # adiciona o item na mochila
#         capacidade -= pesos[melhor]
#         valor_total += valores[melhor]
#         mochila.append(itens[melhor])

#         # remove o item da lista de itens
#         itens.pop(melhor)
#         beneficios.pop(melhor)
#         valores.pop(melhor)
#         pesos.pop(melhor)

#     return valor_total, mochila


def BinGreedy(capacidade: int,
            itens: list[int],
            valores : list[int],
            pesos : list[int], 
            n : int):
    # 1: Mochila = {} 
    Mochila = [-1] * n
    qtd_mochila = 0
    
    # 2: c = 0
    peso_atual = 0
    
    # 3: Beneficio = 0
    Beneficio = 0
    
    # 4, 5, 6: for i <- 1 to n do...
    B = [0.0] * n
    for i in range(n):
        B[i] = valores[i] / pesos[i] if pesos[i] > 0 else float('inf')
        
    itens_avaliados = 0
    
    # 7: while (c < C) e (Ainda houver itens para serem avaliados) do
    while peso_atual < capacidade and itens_avaliados < n:
        
        # 8: Selecionar o item S_i com o maior custo-benefício (B_i)
        maior_B = -1.0
        i_selecionado = -1
        
        for i in range(n):
            if B[i] > maior_B:
                maior_B = B[i]
                i_selecionado = i
                
        # Proteção caso não haja mais itens válidos
        if i_selecionado == -1:
            break
            
        # 9: if W_i <= (C - c) then
        if pesos[i_selecionado] <= (capacidade - peso_atual):
            # 10: Mochila U S_i 
            Mochila[qtd_mochila] = itens[i_selecionado]
            qtd_mochila += 1
            
            # 11: Beneficio += V_i
            Beneficio += valores[i_selecionado]
            
            # 12: c += W_i
            peso_atual += pesos[i_selecionado]
            
        # 13, 14, 15: else Descarta o item S_i
        # O descarte (tanto de quem entrou quanto de quem não coube) é feito anulando o B_i
        B[i_selecionado] = -1.0
        itens_avaliados += 1
            
    # 17: return Beneficio, Mochila
    return Beneficio, Mochila[:qtd_mochila]

        