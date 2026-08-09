from time import perf_counter
import matplotlib
matplotlib.use('Agg')  # backend sem GUI — renderiza direto em arquivo, sem abrir janela
import matplotlib.pyplot as plt
from EstrategiaGulosa import BinGreedy
from ForcaBruta import FB
from utils import listar_caminhos_dos_arquivos


def ler_entrada(caminho : str):
    """Le a instancia do problema no caminho e retorna a capacidade da mochila, os valores e pesos de cada item
    
        Args:
            caminho (str): caminho para a instancia (input/Mochila<N>.txt)
    
        Returns:
            capacidade (int): Capacidade da mochila do problema
            valores (list[int]): Lista dos valores de cada item
            pesos (list[int]): Lista dos pesos de cada item
        """

    with open(caminho, "r") as f:
        capacidade, valores, pesos = f.readlines() # Le linhas

        # Transforma em listas de inteiros
        capacidade = int(capacidade.split()[0])
        valores = [int(x) for x in valores.split()]
        pesos = [int(x) for x in pesos.split()]

    return capacidade, valores, pesos
        

def main():

    # Ler caminhos
    caminhos = listar_caminhos_dos_arquivos()
    # caminhos = [caminhos[i] for i in range(7)]
    print(caminhos)

    ordem_execucao = [10,12,14,16,20,30,40,50,100,200,300,500,750,1000,1250,1500,2000,2500,3000,4000,5000]

    algoritmos = [BinGreedy, FB]

    # Dicionário: nome_algoritmo -> lista de tempos médios (um por instância)
    medias = {alg.__name__: [] for alg in algoritmos}

    for caminho in caminhos: # Para cada instancia do problema

        # Le a instancia.
        instancia = ler_entrada(caminho)

        nome_caminho = caminho.removeprefix("input\\")
        print(f"\nProblema : {nome_caminho}")

        for algoritmo in algoritmos: # Para cada algoritmo

            # Se tamanho da mochila maior que 30, pula a execução do FB
            if algoritmo.__name__ == "FB" and len(instancia[1]) > 30:
                continue

            print(f"    Algoritmo : {algoritmo.__name__}")

            tempo_total = 0
            iteracoes = 6
            for i in range(iteracoes):

                # Instancia para cada iteração, pois os vetores são alterados internamente
                capacidade_maxima = instancia[0]
                valores = instancia[1].copy()
                pesos = instancia[2].copy()
                itens = [x for x in range(len(valores))]

                inicio = perf_counter()
                retorno = algoritmo(capacidade=capacidade_maxima,
                          valores=valores,
                          pesos=pesos,
                          itens=itens,
                          n=len(valores))
                fim = perf_counter()

                if i != 0: # Descarta a primeira iteração (Especificação do trabalho)
                    tempo_total += fim - inicio

            # Calcula e guarda a média das iteracoes execuções restantes
            duracao_media = tempo_total / (iteracoes - 1) * 1000 # -1 por causa da iteração descartada e multiplica por 1000 para converter para milissegundos
            medias[algoritmo.__name__].append(duracao_media)
            print(f"    Tempo : {duracao_media}ms\n")

    # Separa os tempos e tamanhos de cada algoritmo
    tempos_BG = medias['BinGreedy']
    tempos_FB = medias['FB'] 
    
    tamanhos_BG = ordem_execucao[:len(tempos_BG)]
    tamanhos_FB = ordem_execucao[:len(tempos_FB)]


    # Gráfico 1: Comparação BGxFB até a mochila 30
    plt.figure(figsize=(10, 6))

    plt.plot(tamanhos_BG[:len(tamanhos_FB)], tempos_BG[:len(tempos_FB)], marker='o', label='BinGreedy')
    plt.plot(tamanhos_FB, tempos_FB, marker='s', label='Força Bruta')

    plt.xlabel('Tamanho da entrada (nº de itens)')
    plt.ylabel('Tempo médio de execução (ms)')
    plt.title('Comparação: Estratégia Gulosa x Força Bruta')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig('comparacao_BGxFB_ate_30.png')
    plt.yscale('log')
    plt.savefig('comparacao_BGxFB_ate_30_log.png')
    plt.close()

    # Gráfico 2: BG até a última mochila

    plt.figure(figsize=(10, 6))
    
    plt.plot(tamanhos_BG, tempos_BG, marker='o', label='BinGreedy', color='blue')
    
    plt.xlabel('Tamanho da entrada (nº de itens)')
    plt.ylabel('Tempo médio de execução (ms)')
    plt.title('Estratégia Gulosa')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    # Salva versão normal e logarítmica
    plt.savefig('BG_completo.png')
    plt.yscale('log')
    plt.savefig('BG_completo_log.png')
    plt.close()


    print("\nGráficos salvos em:")
    print("  comparacao_BGxFB_ate_30.png")
    print("  comparacao_BGxFB_ate_30_log.png")
    print("  BG_completo.png")
    print("  BG_completo_log.png")


if __name__ == "__main__":
    main()