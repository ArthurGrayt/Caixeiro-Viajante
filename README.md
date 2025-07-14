# Otimização de Rotas: Problema do Caixeiro Viajante (PCV) com Vizinho Mais Próximo 🗺️

---
## Sobre o Projeto

O Problema do Caixeiro Viajante é um desafio clássico que busca encontrar a rota mais eficiente para visitar um conjunto de lugares uma única vez e retornar ao ponto de partida. Como encontrar a solução perfeita pode ser muito complexo, especialmente com muitas cidades, optamos pela heurística do Vizinho Mais Próximo. Ela é rápida e gera uma boa solução, mesmo que não seja a melhor possível.

## Como Funciona

1.  **Começo:** A viagem inicia em uma cidade escolhida.
2.  **Próximo Passo:** De onde você está, vá para a cidade não visitada que for mais próxima.
3.  **Construção da Rota:** Repita isso até visitar todas as cidades.
4.  **Fim:** Retorne à cidade de onde você partiu para fechar o ciclo.

## Como Rodar

1.  **Baixe o código:**
    ```bash
    git clone [https://github.com/SeuUsuario/NomeDoSeuRepositorio.git](https://github.com/SeuUsuario/NomeDoSeuRepositorio.git)
    cd NomeDoSeuRepositorio
    ```
2.  **Execute:**
    ```bash
    python seu_arquivo.py # (Troque 'seu_arquivo.py' pelo nome do seu arquivo)
    ```
