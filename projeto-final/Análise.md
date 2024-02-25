### Importações

Esta linha importa o módulo ast, que significa Árvores de Sintaxe Abstrata. Este módulo é usado para analisar o código Python em uma árvore de sintaxe abstrata (AST),
permitindo-nos analisar a estrutura e os componentes do código programaticamente.
```python
import ast
```

### Classes
Esta classe CodeAnalyzer é uma subclasse de ast.NodeVisitor, que nos permite percorrer a AST e realizar ações com base nos nós encontrados.
Ela inicializa dois dicionários: operations para rastrear a contagem de várias operações no código, e loops para rastrear a contagem de diferentes tipos de loops.

```python
class CodeAnalyzer(ast.NodeVisitor):
    """Classe para analisar o código fonte Python e extrair informações sobre suas operações e loops."""

    def __init__(self):
        """Inicializa os contadores de operações e loops."""
        self.operations = {
            'Assign': 0,      # Contador para atribuições
            'AugAssign': 0,   # Contador para atribuições aumentadas
            'BinOp': 0,       # Contador para operações binárias
            'UnaryOp': 0,     # Contador para operações unárias
            'Compare': 0,     # Contador para comparações
            'Call': 0         # Contador para chamadas de função
        }
        self.loops = {
            'For': 0,         # Contador para loops 'for'
            'nested For': 0,  # Contador para loops 'for' aninhados
            'While': 0,       # Contador para loops 'while'
            'nested While': 0 # Contador para loops 'while' aninhados
        }
```

### Métodos
O método ***visit*** é chamado para cada nó na AST. Ele verifica o tipo do nó e atualiza os dicionários operations e loops de acordo. Para nós FunctionDef, ele visita recursivamente seus filhos.
Para nós For e While, ele incrementa os contadores de loop correspondentes e verifica loops aninhados. Para outros nós, ele atualiza os contadores de operação, se aplicável, e continua a visitar seus filhos.
Esta parte do código é crucial para percorrer a AST e coletar informações sobre a estrutura e os componentes do código.

```python
    def visit(self, node):
        """Visita os nós da AST e atualiza os contadores de operações e loops."""
        if isinstance(node, ast.FunctionDef):
            # Se o nó for uma definição de função, visita seus nós filhos
            self.generic_visit(node)
        elif isinstance(node, ast.For):
            # Se o nó for um loop 'for', atualiza os contadores
            self.loops['For'] += 1
            # Verifica se há loops 'for' aninhados e atualiza o contador correspondente
            nested_level = has_nested_loops(node)
            if nested_level > self.loops['nested For']:
                self.loops['nested For'] = nested_level
            self.generic_visit(node)
        elif isinstance(node, ast.While):
            # Se o nó for um loop 'while', atualiza os contadores
            self.loops['While'] += 1
            # Verifica se há loops 'while' aninhados e atualiza o contador correspondente
            nested_level = has_nested_loops(node)
            if nested_level > self.loops['nested While']:
                self.loops['nested While'] = nested_level
            self.generic_visit(node)
        else:
            # Se o nó não for uma definição de função, loop 'for' ou 'while', atualiza os contadores de operações
            node_type = type(node).__name__
            if node_type in self.operations:
                self.operations[node_type] += 1
            self.generic_visit(node)

```
 

***has_nested_loops*** é um método recursivo crucial para percorrer a AST (Abstract Syntax Tree) em busca de loops aninhados. Ele aceita dois parâmetros: node, que representa o nó atual da AST que está sendo analisado,
e level, que é um parâmetro opcional representando o nível atual de aninhamento de loops. Por padrão, o nível é definido como 0. Antes de entrar na recursão, a função verifica se o nó atual é um loop (um loop for ou while).
Se não for, a função retorna o nível atual de aninhamento de loops. Se o nó atual for um loop, a função itera sobre os nós filhos desse loop e chama recursivamente a si mesma para cada nó filho,
aumentando o nível de aninhamento em 1 para cada loop encontrado. Durante a recursão, a função mantém o controle do nível máximo de aninhamento de loops encontrados até o momento. Quando a busca é concluída, ela retorna o nível máximo de aninhamento.

```python
def has_nested_loops(node, level=0):
    """Verifica se há loops aninhados em um nó da AST."""
    if isinstance(node, ast.For) or isinstance(node, ast.While):
        # Se o nó for um loop 'for' ou 'while', verifica seus nós filhos recursivamente
        max_level = level
        for child_node in ast.iter_child_nodes(node):
            max_level = max(max_level, has_nested_loops(child_node, level + 1))
        return max_level
    return level
```

O método ***analyze_code_from_file*** recebe o nome de um arquivo contendo código-fonte Python como entrada. Ele abre o arquivo, lê o conteúdo e, em seguida,utiliza a função ast.parse() para analisar
o código-fonte e gerar uma Árvore de Sintaxe Abstrata (AST) correspondente. Em seguida, cria uma instância da classe CodeAnalyzer e chama o método visit() da classe, passando a raiz da AST como argumento.
Isso inicia o processo de análise do código, onde a classe CodeAnalyzer visitará todos os nós da AST e contará as operações e loops presentes no código.

```python
def analyze_code_from_file(filename):
    """Analisa o código de um arquivo e extrai informações sobre suas operações e loops."""
    with open(filename, 'r') as file:
        code = file.read()
    tree = ast.parse(code)
    # Instancia um objeto da classe CodeAnalyzer e visita a AST do código
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)
    # Retorna os resultados da análise
    return analyzer.operations, analyzer.loops
```

A função ***print_asymptotic_notation*** é responsável por imprimir a notação assintótica com base nos loops identificados durante a análise. Ela calcula a notação assintótica com base no número máximo de loops aninhados encontrados
e imprime o resultado na saída padrão. Esta função é chamada no final do processo de análise para fornecer uma visão geral da complexidade do algoritmo representado pelo código-fonte fornecido.

```python
def print_asymptotic_notation(loops):
    """Imprime a notação assintótica com base nos loops identificados."""
    max_nested_for = loops.get('nested For', 0)
    max_nested_while = loops.get('nested While', 0)

    if max_nested_for == 0 and max_nested_while == 0:
        print("O(1)")
    elif max_nested_for == 0:
        print(f"O(n^{max_nested_while})")
    elif max_nested_while == 0:
        print(f"O(n^{max_nested_for})")
    else:
        print(f"O(n^{max_nested_for + max_nested_while})")
```

Finalmente, a coordenação e exibição dos dados é chamada na função principal

```python
if __name__ == "__main__":
    """Função principal para análise do código de um arquivo."""
    file_path = "file.txt"
    operations, loops = analyze_code_from_file(file_path)

    print("Operações Identificadas:")
    for op, count in operations.items():
        print(f"{op}: {count}")

    print("\nLoops Identificados:")
    for loop, count in loops.items():
        if "nested" in loop:
            print(f"{loop}: {count}")
        elif "For" in loop or "While" in loop:
            if has_nested_loops(loop):
                print(f"{loop}->aninhado {loop}: {count}")
            else:
                print(f"{loop}: {count}")

    print("\nNotação Assintótica:")
    print_asymptotic_notation(loops)
```
