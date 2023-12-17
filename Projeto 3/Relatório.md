# Relatório - Projeto 3

## Introdução
A criptografia desempenha um papel essencial na segurança da informação, protegendo dados sensíveis por meio de técnicas como a criptografia de ponta a ponta.
Ao garantir a confidencialidade por meio da transformação dos dados em formato ilegível, a criptografia assegura que apenas destinatários autorizados possam acessar as informações.
Além disso, a integridade dos dados é mantida através de funções hash e assinaturas digitais, fornecendo uma camada adicional de confiança ao verificar a autenticidade das informações transmitidas.
A gestão segura de chaves criptográficas e a adaptação constante a avanços tecnológicos, como na pesquisa de criptografia pós-quântica, reforçam a posição crucial da criptografia na preservação da segurança em um mundo digital em constante evolução.

Este projeto visa explorar um método de criptografia chamado de cifra xor. Na cifra xor uma porção de dados é convertida em bits, subsequentemente é feita a operação XOR nos bits dessa porção de dados comparando com uma dada chave de criptografia.
O resultado é uma porção de dados que pode ser decifrado utilizando a mesma operação xor nos dados cifrados, utilizando a mesma chave.
Por possuir uma operação na qual a mesma chave cifra e decifra os dados, este método pertence à categoria de chave simétrica.

##  Análise de Complexidade de Algoritmos
A análise de complexidade de algoritmos é um processo fundamental na ciência da computação que envolve a avaliação da eficiência e dos requisitos de recursos de um algoritmo em função do tamanho de sua entrada.
O objetivo é compreender como o desempenho do algoritmo se comporta com o aumento dos dados de entrada. Essa análise geralmente se concentra em dois aspectos:
a complexidade temporal, que representa o tempo computacional necessário para a execução do algoritmo, e a complexidade espacial, que reflete a quantidade de memória que o algoritmo consome.
A notação "big O" é comumente utilizada para expressar a complexidade algorítmica, proporcionando uma forma concisa de descrever o limite superior ou o cenário de pior caso do crescimento do algoritmo.
Através da análise de complexidade, programadores e engenheiros podem tomar decisões informadas sobre a seleção, otimização e design de algoritmos, contribuindo assim para o desenvolvimento de soluções de software mais eficientes e escaláveis.

Dentro do escopo da análise de algoritmos, a análise assintótica consiste na abstração da função avaliada quando o conjunto de dados na qual ela opera se aproxima do infinito.
Como dito anteriormente, a principal forma de representação dos resultados obtidos dessa análise é a notação "Big O".
No que se refere ao algoritmo proposto pelo autor deste relatório, sua complexidade de tempo e espaço é representada pela função O(n). Isto significa que ela cresce linearmente conforme o conjunto de dados cresce.

Do outro lado do espectro de técnicas de análise, enquanto a análise assintótica é uma medida teórica obtida através da abstração, as técnicas de prova visam aferir a corretude do algoritmo de maneira mais prática através de testes diretos.
A utilização de ambas a análise assintótica, e as técnicas de prova se mostram essenciais no desenho e análise de algoritmos, explorando tanto sua eficiência quanto a sua corretude,
resultando em uma técnica de desenvolvimento e produção de programas de computador mais robusta e eficaz.

No contexto das técnicas de prova, a prova de cotas inferiores consiste na determinação do requerimento mínimo de recursos de sistema, como tempo e memória, requerido por um algoritmo para executar dada operação.
Continuando a análise do algoritmo proposto anteriormente, exploraremos sua conta inferior.

### Definição do problema:
Criptografar uma mensagem usando um cifra XOR recursiva com um texto simples (pt) e uma chave (key) fornecidos.

### Especificar Restrições:
Vamos considerar um cenário em que o comprimento do texto simples (len(pt)) e o comprimento da chave (len(key)) são fixos.

### Identificar Propriedades-Chave:
Concentre-se na natureza recursiva da operação XOR e na relação entre o tamanho da entrada e o tamanho da chave.

### Construir uma Prova:

#### Ideia da Prova:
A cifra XOR recursiva processa cada byte do texto simples sequencialmente, aplicando a operação XOR com o byte correspondente da chave.
Como cada byte é processado independentemente, qualquer algoritmo que tente criptografar uma mensagem com uma abordagem semelhante deve executar pelo menos tantas operações XOR quantos bytes houver no texto simples.

#### Notação Matemática:
Seja n o comprimento do texto simples. Podemos expressar o limite inferior como Ω(n),
indicando que qualquer algoritmo que criptografe uma mensagem usando uma cifra XOR recursiva deve ter uma complexidade de tempo pelo menos proporcional ao comprimento do texto simples.

### Expressar Usando Notação:

#### Notação de Limite Inferior: Ω(n)

Em resumo, a prova de limite inferior para a cifra XOR recursiva sugere que, no pior caso,
qualquer algoritmo que empregue uma abordagem semelhante de XOR recursiva deve ter uma complexidade de tempo pelo menos linear no comprimento do texto simples.
Isso estabelece uma base para o número mínimo de operações necessárias para tarefas de criptografia desse tipo.

## Medidas Empíricas de Performance

Medidas empíricas de desempenho referem-se a medições e avaliações do desempenho real de um sistema, aplicação ou algoritmo sob condições do mundo real. Essas medidas são obtidas por meio de observação prática,
experimentação e coleta de dados, em vez de análise teórica.

As medidas empíricas de desempenho são cruciais para avaliar como o software se comporta na prática, identificar possíveis gargalos e tomar decisões informadas sobre otimizações. Exemplos comuns de medidas empíricas de desempenho incluem tempo de execução, uso de memória, tempo de resposta, produtividade e outros indicadores quantitativos que fornecem insights sobre a eficiência e eficácia de um sistema de software.

Ao coletar e analisar dados empíricos de desempenho, desenvolvedores e administradores de sistemas podem identificar áreas para melhorias, validar a eficácia de otimizações e tomar decisões informadas sobre a escalabilidade e confiabilidade de aplicativos de software em cenários do mundo real. Essa abordagem empírica complementa a análise teórica e ajuda a garantir que o software tenha bom desempenho em ambientes diversos e dinâmicos.


### Uso de Relações de Recorrência:
No contexto da ciência da computação e matemática, uma relação de recorrência é uma maneira de definir uma sequência de valores em que cada termo na sequência é definido em termos de um ou mais termos anteriores.
A relação de recorrência fornece uma maneira de expressar a relação entre o valor de uma função em um determinado ponto e seus valores em pontos anteriores. Relações de recorrência são frequentemente usadas na análise de algoritmos, especialmente ao avaliar a complexidade temporal ou espacial de algoritmos recursivos.

Aqui está um exemplo simples de uma relação de recorrência:
T(n) = 2T(n/2) + 1

Nesta relação, T(n) representa a complexidade temporal de um algoritmo, e é definido em termos do dobro da complexidade temporal do algoritmo com metade do tamanho de entrada (T(n/2)), mais um termo constante (1).
Resolver relações de recorrência é uma tarefa comum na análise de algoritmos, e frequentemente envolve encontrar soluções em forma fechada ou usar técnicas como o Teorema Mestre para analisar o comportamento assintótico dos algoritmos.

A relação de recorrência para o algoritmo do cifra XOR em termos de complexidade temporal T(n) pode ser expressa da seguinte forma: 

T(n)=T(n−1)+Θ(1)

- T(n): Representa a complexidade temporal do algoritmo para uma entrada de tamanho n.  
- T(n−1): Representa a complexidade temporal para um tamanho de entrada menor n−1 quando o algoritmo é chamado recursivamente nos elementos restantes.  
- Θ(1): Representa o tempo constante necessário para a operação XOR e outras operações de tempo constante dentro da função.  

Essa relação de recorrência captura a natureza recursiva do algoritmo, onde a complexidade temporal para uma entrada de tamanho n está diretamente relacionada à complexidade temporal para uma entrada de tamanho n−1,
somada a uma quantidade constante de tempo para a operação XOR.

É importante observar que a análise assume tempo constante para a operação XOR e não leva em consideração outros fatores que poderiam afetar a complexidade temporal, como o custo das chamadas de função ou outras operações dentro da função. Para uma análise mais detalhada, esses fatores precisariam ser considerados.

## Comparação entre forma iterativa e recursiva:

### Algoritmo Recursivo XOR:

**Complexidade Temporal:**  
- T(n)=T(n−1)+Θ(1)

**Complexidade Espacial:**  
- O algoritmo recursivo XOR gera espaço na pilha de chamadas para cada chamada recursiva, levando a uma possível complexidade espacial de O(n) no pior caso.

**Overhead da Recursão:**  
- Algoritmos recursivos podem ter overhead adicional devido às chamadas de função e gerenciamento da pilha de chamadas.

**Facilidade de Compreensão:**  
- Algoritmos recursivos podem ser mais intuitivos para certos problemas e mais fáceis de entender conceptualmente.

### Algoritmo Iterativo XOR:

**Complexidade Temporal:**  
- T(n) = Θ(n)

**Complexidade Espacial:**  
- O algoritmo iterativo XOR tipicamente possui complexidade espacial constante (\(\Theta(1)\)) por não depender de chamadas recursivas.

**Overhead da Iteração:**  
- Algoritmos iterativos podem envolver controle explícito de loop, potencialmente resultando em código mais limpo sem o overhead de chamadas recursivas.

**Facilidade de Compreensão:**  
- Algoritmos iterativos são frequentemente mais diretos e eficientes em termos de complexidade espacial.

### Comparação Geral:

1. **Complexidade Temporal:**
   - **Recursivo:** O(n^2) devido ao overhead recursivo.
   - **Iterativo:** O(n) com melhor eficiência.

2. **Complexidade Espacial:**
   - **Recursivo:** O(n) devido ao uso da pilha de chamadas.
   - **Iterativo:** Θ(1) com uso de espaço constante.

3. **Recursão vs. Iteração:**
   - **Recursivo:** Mais intuitivo, mas potencialmente com maior overhead.
   - **Iterativo:** Mais eficiente em termos de tempo e espaço.

4. **Otimizações:**
   - Algoritmos recursivos podem se beneficiar da otimização de recursão de cauda em certas linguagens de programação.
   - Algoritmos iterativos frequentemente têm fluxo de controle direto sem a necessidade de otimização.

5. **Casos de Uso:**
   - **Recursivo:** Adequado para problemas com uma estrutura recursiva natural.
   - **Iterativo:** Preferível pela eficiência e simplicidade em muitos casos.

**Conclusão:**
A escolha entre os algoritmos XOR recursivo e iterativo depende dos requisitos específicos do problema e das compensações entre clareza, eficiência e uso de espaço. Enquanto algoritmos recursivos podem ser mais intuitivos, soluções iterativas frequentemente oferecem melhor desempenho e menor complexidade espacial. Deve-se considerar as características dos dados de entrada e a linguagem de programação utilizada.


### Refinamento de Algoritmo
A seguir, exemplificarei algumas das mais utilizadas técnica de refino de algoritmos

#### Recursão:
Recursão é um conceito em programação em que uma função chama a si mesma para resolver um problema. A ideia é dividir um problema complexo em subproblemas menores e resolver cada subproblema recursivamente até atingir um caso base.

**Pontos chave:**
- **Casos Base:** Cada chamada recursiva deve eventualmente atingir um caso base que não requer mais subdivisão.
- **Empilhamento de Chamadas:** As chamadas de função são empilhadas na pilha de chamadas até que os casos base sejam alcançados, momento em que as chamadas começam a ser desempilhadas.

#### Dividir para Conquistar:
Dividir para conquistar é um paradigma de resolução de problemas em que um problema é dividido em subproblemas menores, resolvidos independentemente, e então as soluções são combinadas para resolver o problema original.

**Pontos chave:**
- **Divisão:** Divide-se o problema principal em subproblemas menores.
- **Conquista:** Resolve-se cada subproblema de maneira independente.
- **Combinação:** Combina-se as soluções dos subproblemas para obter a solução do problema original.

#### Programação Dinâmica:
Programação dinâmica é uma técnica de otimização que resolve problemas dividindo-os em subproblemas menores e armazenando as soluções desses subproblemas para evitar recálculos desnecessários.

**Pontos chave:**
- **Memorização:** Armazena-se as soluções dos subproblemas em uma tabela para reutilização.
- **Subestrutura Ótima:** O problema global pode ser otimizado combinando soluções otimizadas dos subproblemas.

#### Programação Gulosa:
A programação gulosa é um paradigma em que, em cada etapa, faz-se a escolha localmente ótima na esperança de encontrar uma solução globalmente ótima para o problema.

**Pontos chave:**
- **Escolha Ótima Local:** Faz-se a escolha que parece ser a melhor naquele momento, sem reconsiderar escolhas anteriores.
- **Não Volta Atrás:** Uma vez feita uma escolha, não é reconsiderada.

#### Backtracking:
Backtracking é uma técnica de busca que tenta construir todas as soluções possíveis para um problema, escolhendo uma opção por vez e retrocedendo quando não há mais opções viáveis.

**Pontos chave:**
- **Construção Incremental:** Constrói-se incrementalmente uma solução parcial.
- **Testes de Viabilidade:** A cada etapa, verifica-se se a solução parcial atende aos requisitos.
- **Retrocesso (Backtrack):** Se uma solução parcial não pode ser estendida para uma solução válida, retrocede-se para a escolha anterior.

Essas técnicas são fundamentais em algoritmos e resolução de problemas, cada uma sendo adequada para diferentes tipos de problemas e situações.
