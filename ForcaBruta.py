import time
import bisect

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

    tempo = time.perf_counter()
    # Testa todas as combinações, cada valor de i representa uma combinação diferente de itens)
    for i in range(2**n):
        # if i % 100000 == 0:
        #     print(f"\n{i/100000}/{2**n/100000}")
        #     print(f"{time.perf_counter() - tempo}s")
        #     print(f"{i/(time.perf_counter() - tempo)} iteracoes por segundo")
        mochila_atual = []
        peso_atual = 0
        valor_atual = 0

        # Verifica quais itens estão incluídos na combinação atual
        for j in range(n):
            if (i >> j) & 1: # Move os bits do i para direita em j posições e verifica se o bit menos significativo é 1
                peso_atual += pesos[j] # Contabiliza o peso
                
                if peso_atual > capacidade:
                    break
                    
                valor_atual += valores[j] # Contabiliza o valor
                mochila_atual.append(itens[j]) # Adiciona o item à combinação atual

        # Verifica se a solução atual é melhor que a melhor encontrada até agora
        if valor_atual > melhor_valor:
            melhor_valor = valor_atual
            melhor_mochila = mochila_atual

    return melhor_valor, melhor_mochila

def FB2(capacidade: int, itens: list[int], valores: list[int], pesos: list[int], n: int):
    """
    Força Bruta com Backtracking e Poda de Peso.

    Explora a mesma árvore de decisões binárias que a FB (incluir/excluir cada item),
    porém utiliza poda: quando o peso acumulado excede a capacidade da mochila,
    todo o ramo filho é abandonado imediatamente — sem precisar continuar explorando
    os itens restantes daquele ramo.

    O progresso é calculado pelo método de intervalo recursivo:
    cada chamada recebe [prog_inicio, prog_fim] representando sua fatia do espaço
    de busca de 0% a 100%. Ao bifurcar, a metade esquerda (incluir) fica com a
    primeira metade do intervalo e a metade direita (excluir) com a segunda.
    Assim o % exibido reflete a posição real na árvore, não um contador aproximado.

    Complexidade: O(2^n) no pior caso (sem poda efetiva);
                  muito melhor na prática graças às podas.
    """

    melhor = [0, []]  # [melhor_valor, melhor_mochila] — lista para permitir mutação dentro da função interna

    tempo_inicio = time.perf_counter()

    # Profundidade a partir da qual os prints de progresso são emitidos.
    # Valor 4 → 2^4 = 16 checkpoints (0%, 6.25%, 12.5%, ..., 93.75%)
    # Aumente para mais granularidade, diminua para menos prints.
    PROFUNDIDADE_PRINT = 25

    def backtrack(i: int, peso_atual: int, valor_atual: int, mochila: list[int],
                  prog_inicio: float, prog_fim: float):
        """
        Percorre recursivamente a árvore de decisão a partir do item de índice i.

        Args:
            i           : índice do item sendo considerado neste nível da recursão
            peso_atual  : soma dos pesos dos itens já incluídos na mochila
            valor_atual : soma dos valores dos itens já incluídos na mochila
            mochila     : lista dos itens incluídos até o momento (por referência)
            prog_inicio : início do intervalo de progresso desta chamada (0.0 a 1.0)
            prog_fim    : fim do intervalo de progresso desta chamada (0.0 a 1.0)
        """

        # # ── Print de progresso ────────────────────────────────────────────────
        # # Imprime ao entrar nos primeiros PROFUNDIDADE_PRINT níveis da árvore,
        # # mostrando o % real da posição na árvore de busca e o tempo decorrido.
        # if i < PROFUNDIDADE_PRINT:
        #     decorrido = time.perf_counter() - tempo_inicio
        #     print(f"    [{prog_inicio * 100:6.2f}%] — {decorrido:.3f}s decorridos")

        # ── Poda de Peso ──────────────────────────────────────────────────────
        # Se o peso atual já ultrapassou a capacidade, qualquer extensão desse
        # ramo também será inválida → abandona toda a subárvore
        if peso_atual > capacidade:
            return

        # ── Caso Base: todos os itens foram decididos ─────────────────────────
        if i == n:
            if valor_atual > melhor[0]:
                melhor[0] = valor_atual
                melhor[1] = mochila[:]  # copia o estado atual da mochila
            return

        # Ponto médio divide o intervalo entre os dois ramos filhos
        prog_mid = (prog_inicio + prog_fim) / 2

        # ── Ramificação: inclui o item i (metade esquerda do intervalo) ───────
        mochila.append(itens[i])
        backtrack(i + 1, peso_atual + pesos[i], valor_atual + valores[i], mochila,
                  prog_inicio, prog_mid)
        mochila.pop()  # desfaz a inclusão antes de explorar a exclusão

        # ── Ramificação: exclui o item i (metade direita do intervalo) ────────
        backtrack(i + 1, peso_atual, valor_atual, mochila,
                  prog_mid, prog_fim)

    backtrack(0, 0, 0, [], 0.0, 1.0)
    return melhor[0], melhor[1]


def FB3(capacidade: int, itens: list[int], valores: list[int], pesos: list[int], n: int):
    """
    Força Bruta Meet in the Middle — versão otimizada para memória.

    Divide os n itens em duas metades A (itens 0..meio-1) e B (itens meio..n-1)
    e ainda enumera exaustivamente todas as combinações de cada metade (força bruta).

    Otimizações de memória em relação à versão ingênua:

      1. Máscaras de bits no lugar de listas de itens:
         Cada subconjunto é representado por um inteiro (máscara) em vez de uma
         lista Python. Isso reduz ~10x o uso de memória por subconjunto,
         pois uma lista de k itens custa ~56 + k×28 bytes, enquanto uma máscara
         custa ~28 bytes independentemente do número de itens.

      2. Metade A processada on-the-fly:
         Os subconjuntos de A são gerados um a um e imediatamente combinados com B.
         Nenhum subconjunto de A fica armazenado em memória, reduzindo o pico à
         metade do custo total.

      3. Liberação antecipada de b_data:
         A lista bruta de B é apagada assim que o envelope é construído,
         liberando memória antes da fase de combinação com A.

      4. Reconstrução no final:
         Os itens da melhor solução são recuperados das duas máscaras vencedoras
         apenas uma vez, ao terminar.

    Memória estimada para n=50:
      Pico (durante construção do envelope): ~3–4 GB
      Após liberação de b_data:              ~1–2 GB

    Complexidade: O(n * 2^(n/2)) tempo,  O(2^(n/2)) espaço
    """

    meio  = n // 2    # ponto de divisão: A = [0..meio-1], B = [meio..n-1]
    tam_a = meio
    tam_b = n - meio

    # # ── Fase 1: Enumerar todos os subsets de B, armazenando apenas a máscara ──
    # # Cada entrada: (peso_total, valor_total, máscara_inteira)
    # # A máscara codifica quais itens de B estão incluídos (bit j = item meio+j)
    # print(f"    [1/3] Enumerando {1 << tam_b:,} subsets da Metade B (itens {meio}..{n-1})...")
    b_data = []

    for mask in range(1 << tam_b):      # itera por todas as 2^tam_b combinações
        peso_atual  = 0
        valor_atual = 0

        for j in range(tam_b):
            if (mask >> j) & 1:         # bit j ligado → item (meio+j) está incluído
                idx = meio + j
                peso_atual  += pesos[idx]
                valor_atual += valores[idx]

        if peso_atual <= capacidade:    # descarta apenas combinações impossíveis
            b_data.append((peso_atual, valor_atual, mask))

    # Ordena por peso para permitir busca binária depois
    # (tuplas ordenam pelo primeiro elemento por padrão)
    b_data.sort()

    # ── Fase 2: Construir envelope de valor máximo sobre B ordenado ───────────
    # Ao percorrer B em ordem crescente de peso, registra:
    #   pesos_B[i]    : peso do i-ésimo subset válido de B
    #   max_vals_B[i] : maior valor alcançável em B com peso <= pesos_B[i]
    #   masks_max_B[i]: máscara do subset de B que atingiu max_vals_B[i]
    # Isso permite, dado um peso_restante, encontrar o melhor complemento
    # de B em O(log n) via busca binária.
    # print(f"    [2/3] Construindo envelope sobre {len(b_data):,} subsets válidos de B...")
    pesos_B     = []
    max_vals_B  = []
    masks_max_B = []

    max_val_so_far    = -1  # maior valor visto até aqui ao percorrer B por peso
    best_mask_so_far  =  0  # máscara do subset que atingiu max_val_so_far

    for peso_b, valor_b, mask_b in b_data:
        if valor_b > max_val_so_far:    # encontrou subset de B com valor ainda maior
            max_val_so_far   = valor_b
            best_mask_so_far = mask_b

        pesos_B.append(peso_b)
        max_vals_B.append(max_val_so_far)
        masks_max_B.append(best_mask_so_far)

    del b_data  # b_data não é mais necessário — libera memória antes de processar A

    # ── Fase 3: Enumerar A on-the-fly e combinar com envelope de B ────────────
    # Subsets de A são gerados um a um: nenhum fica armazenado em memória.
    # Para cada subset de A, a busca binária encontra o melhor complemento de B.
    # print(f"    [3/3] Enumerando {1 << tam_a:,} subsets da Metade A (itens 0..{meio-1}) e combinando...")

    melhor_valor      = 0
    best_mask_a       = 0  # máscara de A da melhor solução encontrada
    best_mask_b_final = 0  # máscara de B que complementa a melhor solução

    for mask_a in range(1 << tam_a):    # itera por todas as 2^tam_a combinações de A
        peso_a  = 0
        valor_a = 0

        for j in range(tam_a):
            if (mask_a >> j) & 1:       # bit j ligado → item j está incluído
                peso_a  += pesos[j]
                valor_a += valores[j]

        if peso_a > capacidade:         # subset de A já excede a capacidade → pula
            continue

        cap_restante = capacidade - peso_a

        # Busca binária: maior índice i tal que pesos_B[i] <= cap_restante
        idx = bisect.bisect_right(pesos_B, cap_restante) - 1

        if idx >= 0:                    # existe ao menos um subset de B que cabe
            valor_total = valor_a + max_vals_B[idx]
            if valor_total > melhor_valor:
                melhor_valor       = valor_total
                best_mask_a        = mask_a
                best_mask_b_final  = masks_max_B[idx]

    # ── Fase 4: Reconstruir a lista de itens a partir das máscaras vencedoras ─
    # Custo trivial: percorre no máximo n bits no total
    mochila = []
    for j in range(tam_a):
        if (best_mask_a >> j) & 1:
            mochila.append(itens[j])
    for j in range(tam_b):
        if (best_mask_b_final >> j) & 1:
            mochila.append(itens[meio + j])

    return melhor_valor, sorted(mochila)


def FB4(capacidade: int, itens: list[int], valores: list[int], pesos: list[int], n: int):
    """
    Força Bruta Meet in the Middle com Poda de Peso.

    Igual ao FB3, mas substitui o loop de máscaras em cada metade por backtracking
    com poda: quando o peso parcial excede a capacidade, toda a subárvore daquele
    ramo é abandonada sem gerar os subsets filhos.

    A poda não descarta nenhuma combinação viável — apenas combinações que já
    excedem a capacidade e nunca seriam ótimas. Ainda é força bruta.

    Ganho prático: depende da relação capacidade/soma_dos_pesos.
      - Mochila apertada (capacidade pequena) → muita poda → grande ganho
      - Mochila folgada (capacidade ≈ soma)   → pouca poda → ganho pequeno

    Complexidade: O(n * 2^(n/2)) pior caso (sem poda efetiva),
                  melhor na prática graças à poda nas enumerações.
    """

    meio  = n // 2
    tam_a = meio
    tam_b = n - meio

    # ── Enumeração com backtracking e poda de peso ────────────────────────────
    def enumerar_com_poda(inicio: int, fim: int) -> list:
        """
        Gera todos os subsets de itens[inicio:fim] com peso <= capacidade.
        Usa backtracking: abandona ramos quando peso parcial já excede a capacidade.
        Retorna lista de (peso_total, valor_total, mask), onde mask codifica
        quais itens locais (0..tamanho-1) estão incluídos (bit j = item inicio+j).
        """
        tamanho = fim - inicio
        subsets = []

        def backtrack(j: int, peso_atual: int, valor_atual: int, mask_atual: int):

            # ── Poda de peso ──────────────────────────────────────────────────
            # Peso já excedeu a capacidade total da mochila.
            # Qualquer item adicional só aumenta o peso, logo toda a subárvore
            # abaixo deste nó é inviável → abandona sem gerar filhos.
            if peso_atual > capacidade:
                return

            # ── Caso base: todos os itens da metade foram decididos ───────────
            if j == tamanho:
                subsets.append((peso_atual, valor_atual, mask_atual))
                return

            idx = inicio + j  # índice global do item sendo decidido

            # Ramificação: inclui o item j (bit j ligado na máscara)
            backtrack(j + 1,
                      peso_atual  + pesos[idx],
                      valor_atual + valores[idx],
                      mask_atual  | (1 << j))

            # Ramificação: exclui o item j (bit j permanece desligado)
            backtrack(j + 1, peso_atual, valor_atual, mask_atual)

        backtrack(0, 0, 0, 0)
        return subsets

    # ── Fase 1: Enumerar B com poda ───────────────────────────────────────────
    # print(f"    [1/3] Enumerando Metade B (itens {meio}..{n-1}) com poda...")
    b_data = enumerar_com_poda(meio, n)
    b_data.sort()  # ordena por peso para permitir busca binária

    # ── Fase 2: Construir envelope de valor máximo sobre B ordenado ───────────
    # Idêntico ao FB3: max_vals_B[i] = melhor valor em B com peso <= pesos_B[i]
    # print(f"    [2/3] Construindo envelope sobre {len(b_data):,} subsets válidos de B...")
    pesos_B     = []
    max_vals_B  = []
    masks_max_B = []

    max_val_so_far   = -1
    best_mask_so_far =  0

    for peso_b, valor_b, mask_b in b_data:
        if valor_b > max_val_so_far:
            max_val_so_far   = valor_b
            best_mask_so_far = mask_b
        pesos_B.append(peso_b)
        max_vals_B.append(max_val_so_far)
        masks_max_B.append(best_mask_so_far)

    del b_data  # libera memória antes de processar A

    # ── Fase 3: Enumerar A com poda e combinar via busca binária ─────────────
    # A é enumerada com backtracking (poda) e cada subset válido é imediatamente
    # combinado com o envelope de B. Nenhum subset de A fica armazenado.
    # print(f"    [3/3] Enumerando Metade A (itens 0..{meio-1}) com poda e combinando...")

    melhor_valor      = 0
    best_mask_a       = 0
    best_mask_b_final = 0

    def combinar_a(j: int, peso_a: int, valor_a: int, mask_a: int):
        nonlocal melhor_valor, best_mask_a, best_mask_b_final

        # ── Poda de peso ──────────────────────────────────────────────────────
        if peso_a > capacidade:
            return

        # ── Caso base: subset de A completo — combina com envelope de B ───────
        if j == tam_a:
            cap_restante = capacidade - peso_a
            idx = bisect.bisect_right(pesos_B, cap_restante) - 1
            if idx >= 0:
                valor_total = valor_a + max_vals_B[idx]
                if valor_total > melhor_valor:
                    melhor_valor      = valor_total
                    best_mask_a       = mask_a
                    best_mask_b_final = masks_max_B[idx]
            return

        # Ramificação: inclui item j de A
        combinar_a(j + 1,
                   peso_a  + pesos[j],
                   valor_a + valores[j],
                   mask_a  | (1 << j))

        # Ramificação: exclui item j de A
        combinar_a(j + 1, peso_a, valor_a, mask_a)

    combinar_a(0, 0, 0, 0)

    # ── Fase 4: Reconstruir itens a partir das máscaras vencedoras ────────────
    mochila = []
    for j in range(tam_a):
        if (best_mask_a >> j) & 1:
            mochila.append(itens[j])
    for j in range(tam_b):
        if (best_mask_b_final >> j) & 1:
            mochila.append(itens[meio + j])

    return melhor_valor, sorted(mochila)
