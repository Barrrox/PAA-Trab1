# Trabalho 1 - Projeto e Análise de Algoritmos (PAA) 2026

## Equipe 5
- André Gustavo Franco
- João Vitor da Silva
- Matheus Barros

## 1. Descrição do Projeto
Este repositório contém a implementação e análise de desempenho de duas abordagens distintas para solucionar o **Problema da Mochila Binária**. O objetivo principal é comparar os tempos de execução cronológicos e a complexidade assintótica teórica dos algoritmos propostos.

## 2. Estratégias Implementadas

### Estratégia Gulosa (BinGreedy)
- **Funcionamento:** O algoritmo avalia iterativamente a melhor razão custo-benefício (valor/peso) para cada item e os adiciona à mochila enquanto houver capacidade disponível, descartando os demais itens.
- **Complexidade Assintótica:** O pior caso possui custo `O(n²)`, possuindo o polinômio `T(n) = 7n² + 42n + 11`.

### Força Bruta (FB)
Uma abordagem exata que testa todas as combinações possíveis para encontrar a solução ótima global.
- **Funcionamento:** Utiliza operações bit a bit para iterar pelas `2^n` combinações diferentes de itens, calculando o peso total e avaliando se a combinação atual gera o maior benefício sem extrapolar a capacidade da mochila.
- **Complexidade Assintótica:** O pior caso possui comportamento exponencial `O(n * 2^n)`, com polinômio `T(n) = 2^n(13n + 11) + 4`.

## 3. Como Executar

**Pré-requisitos:**
- Python 3.x instalado.
- Biblioteca `matplotlib` para a geração dos gráficos (instalar via `pip install matplotlib`).
- Na raiz do projeto (onde se encontra o script `main.py`), execute:
```bash
python main.py > saida.txt
```
O script se encarregará de:
1. Listar as instâncias presentes na pasta `input/`.
2. Executar e tomar os tempos via `perf_counter` de ambos os algoritmos.
3. Imprimir o log de tempos na saida especificada.
4. Salvar os gráficos `comparacao_BGxFB_ate_30.png`, `comparacao_BGxFB_ate_30_log.png`, `BG_completo.png` e `BG_completo_log.png`.
