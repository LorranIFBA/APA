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



