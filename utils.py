from pathlib import Path
import re

def listar_caminhos_dos_arquivos(pasta_input: str = "./input") -> list[str]:
    """"
    Lista os caminhos dos arquivos na pasta especificada, ordenando-os de acordo com a ordem definida em ordem_execucao.
    Se a pasta não existir, retorna uma lista vazia.
    """

    ordem_execucao = [10,12,14,16,20,30,40,50,100,200,300,500,750,1000,1250,1500,2000,2500,3000,4000,5000]

    caminho_pasta = Path(pasta_input)

    # Verifica se a pasta realmente existe e se é um diretório
    if not caminho_pasta.exists() or not caminho_pasta.is_dir():
        print(f"Erro: O diretório '{caminho_pasta}' não foi encontrado.")
        return []

    # Mapeia cada valor à sua posição em ordem_execucao (busca O(1) depois)
    posicao_ordem = {valor: indice for indice, valor in enumerate(ordem_execucao)}

    # Cria uma lista de objetos Path (mantemos como Path até depois de ordenar)
    lista_de_paths = [arquivo for arquivo in caminho_pasta.iterdir() if arquivo.is_file()]

    def extrair_valor(caminho: Path):
        # Extrai o número do nome do arquivo, ex: "Mochila100.txt" -> 100
        match = re.search(r"Mochila(\d+)\.txt", caminho.name)
        return int(match.group(1)) if match else None

    # Ordena com base na posição do valor extraído dentro de ordem_execucao.
    # Arquivos fora do padrão ou com valor não presente no vetor vão para o final,
    # em vez de quebrar a execução.
    lista_de_paths.sort(
        key=lambda p: posicao_ordem.get(extrair_valor(p), len(ordem_execucao))
    )

    return [str(arquivo) for arquivo in lista_de_paths]