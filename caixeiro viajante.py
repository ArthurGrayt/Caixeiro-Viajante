# Criando a matriz das distancias de cidades
matriz_distancias = [
    # Cidades de Destino (Colunas): Cid. 1, Cid. 2, Cid. 3, Cid. 4, Cid. 5
    [0, 2, 1, 4, 9],  # Distâncias da Cidade de Origem: Cid. 1 (índice 0)
    [2, 0, 5, 9, 7],  # Distâncias da Cidade de Origem: Cid. 2 (índice 1)
    [1, 5, 0, 3, 8],  # Distâncias da Cidade de Origem: Cid. 3 (índice 2)
    [4, 9, 3, 0, 2],  # Distâncias da Cidade de Origem: Cid. 4 (índice 3)
    [9, 7, 8, 2, 0],  # Distâncias da Cidade de Origem: Cid. 5 (índice 4)
]

# O número de cidades é determinado pelo tamanho da matriz
num_cidades = len(matriz_distancias)


