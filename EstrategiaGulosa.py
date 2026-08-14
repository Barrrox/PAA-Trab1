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

        