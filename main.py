from time import time
from time import perf_counter
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
    caminhos = [caminhos[i] for i in range(6)]
    #print(caminhos)

    medias_FB = []
    medias_BinGreedy = []

    ordem_execucao = [10,12,14,16,20,50,100,200,300,500,750,1000,1250,1500,2000,2500,3000,4000,5000]


    for caminho in caminhos:# Para cada instancia do problema       

        # Le a instancia. 
        instancia = ler_entrada(caminho)

        caminho = caminho.removeprefix("input\\")
        print(f"\nProblema : {caminho}") 

        

        duracao_media_FB = 0
        duracao_media_BinGreedy = 0

        # Le arquivo da instancia
        for algoritmo in [FB, BinGreedy]:# Para cada algoritmo
            print(f"    Algoritmo : {algoritmo.__name__}") 

            tempo_total = 0
            for i in range(6):

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

                # print(caminho)
                # print(capacidade_maxima)
                # print(retorno[0])
                # input()

                if i != 0: # Descarta a primeira iteração (Espeficação do trabalho)
                    tempo_total += fim - inicio

            # calcular media do tempo desta instância
            if algoritmo == FB:
                duracao_media_FB = tempo_total / 5
                print(f"    Tempo : {duracao_media_FB}s\n")
            else:
                duracao_media_BinGreedy = tempo_total / 5
                print(f"    Tempo : {duracao_media_BinGreedy}s\n")

        # guarda o tempo médio desta instância nas listas
        medias_FB.append(duracao_media_FB)
        medias_BinGreedy.append(duracao_media_BinGreedy)

    # tamanhos correspondentes às instâncias efetivamente processadas
    tamanhos = ordem_execucao[:len(medias_FB)]

    # plotar os graficos tamanho x tempo medio de execução
    plt.figure(figsize=(10, 6))

    plt.plot(tamanhos, medias_FB, marker='o', label='Força Bruta')
    plt.plot(tamanhos, medias_BinGreedy, marker='s', label='Estratégia Gulosa')


    plt.xlabel('Tamanho da entrada (nº de itens)')
    plt.ylabel('Tempo médio de execução (s)')
    plt.title('Tamanho da entrada x Tempo médio de execução')
    plt.legend()


    plt.yscale('log')
    plt.grid(True, which='both', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig('tamanho_x_tempo.png')
    plt.show()


if __name__ == "__main__":
    main()