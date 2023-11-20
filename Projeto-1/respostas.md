# Desenvolvimento do Projeto:

> Desenvolva um algoritmo eficiente para calcular a complexidade de tempo no pior caso para a busca de um produto no estoque. Considere que a busca será realizada pelo nome do produto. Justifique sua resposta e discuta como a ordem influencia na performance do algoritmo.

##### R. Devido a estrutura do algoritmo estar ordenada alfabeticamente, o melhor algoritmo de busca seria 'busca binaria'. Considerando sua utilização, o melhor caso da busca seria o elemento encontrado na posicao do meio da lista, com notação assintótica O(1) e o seu pior caso sendo O(logN). Caso a lista estivesse ordenada de maneira aleatoria, devido a limitaçao da estrutura de dados utilizada, seria necessario uma busca linear, verificando individualmente cada elemento da lista, com notação assintótica O(n).

>Implemente um algoritmo de ordenação que mantenha a lista de produtos do estoque sempre ordenada. Explique como seu algoritmo funciona e por que você escolheu essa abordagem específica para ordenar a lista.
##### R.Utilizei o algoritmo merge sort, pois ele é um algoritmo relativamente simples de implementar, porém é bastante poderoso, tendo uma eficiência boa tanto para casos onde os elementos estão ordenados de maneira aleatória quanto para casos onde os elementos estão relativamente ordenados.

>Desenvolva um algoritmo de busca binária que aproveite a ordenação alfabética da lista de produtos. O algoritmo deve receber como entrada o nome do produto a ser localizado e retornar o identificador único desse produto, caso exista no estoque. Explique como seu algoritmo funciona e justifique por que a busca binária é apropriada neste contexto.

##### R. O algoritmo consiste em determinar o elemento central da coleção de dados, e verificar se este elemento é igual ao elemento sendo buscado. Caso não seja, se ele for menor lexicograficamente, o processo será repetido para a porção do lado esquerdo do elemento central. Caso seja maior, isso será feito para a porção do lado direito. Isso se repetirá até que o elemento seja encontrado, ou não. Caso não seja, ele retornará um valor arbitrário que servirá como marcador de falha.A busca binária é apropriada, pois os dados estão ordenados. Se não estivessem, esse algoritmo nunca iria retornar o valor correto consistentemente.

>Suponha que, ao analisar o desempenho do sistema de gerenciamento de estoque, você percebe que a busca linear está sendo frequentemente utilizada para buscar produtos com nomes similares. Proponha uma otimização para o algoritmo de busca que permita encontrar produtos que começam com uma determinada letra de forma mais eficiente, aproveitando a ordenação alfabética da lista.
##### R. A criaçao de listas separadas com elementos que comecem com a mesma letra facilitaria a utilizacao de algoritmos de busca lineares, pois limitaria o escopo da busca, otimizando o desepemenho. Por exemplo: Lista A[elementos cujo nome comece com a letra A], Lista B[elementos cujo nome comece com a letra B], Lista C[elementos cujo nome comece com a letra C]. Dessa forma, sabendo a letra inicial do produto, bastaria procurar na lista adequada.Entretanto, nos casos onde a busca será feita no corpo completo de elementos, a busca binária deve ser utilizada se possível.


# Análise de Caso Médio:

>Considere que, em média, 80 porcento das buscas no sistema são para produtos que estão entre as 100 primeiras posições alfabéticas. Proponha uma estratégia que tire proveito desse padrão para melhorar o desempenho do algoritmo de busca. Implemente a estratégia e um novo algoritmo e explique como ela otimiza a busca para casos médios.

##### R. Considerando que busca binária deve ser sempre utilizado quando possível, devido à sua superioridade, o mais eficiente é limitar o escopo da busca e continuar utilizando o algoritmo. Portanto a otimização que eu implementei foi criar uma condicao que cheque se a lista é maior que 150 elementos(com uma margem suficientemente grande para maximizar as chances de ocorrência), se ela for, ela irá efetuar uma busca binaria em apenas os 150 primeiros elementos da lista. Se o objeto sendo buscado nao for encontrado, ela efetuará a busca nos elementos restantes. Se a lista for menor que 150 elementos, o algoritmo será efetuado de maneira usual.

