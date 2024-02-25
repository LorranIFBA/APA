import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.operations = {
            'Assign': 0,
            'AugAssign': 0,
            'BinOp': 0,
            'UnaryOp': 0,
            'Compare': 0,
            'Call': 0
        }
        self.loops = {
            'For': 0,
            'nested For': 0,
            'While': 0,
            'nested While': 0
        }

    def visit(self, node):
        if isinstance(node, ast.FunctionDef):
            self.generic_visit(node)
        elif isinstance(node, ast.For):
            self.loops['For'] += 1
            nested_level = self.has_nested_loops(node)
            if nested_level > self.loops['nested For']:
                self.loops['nested For'] = nested_level
            self.generic_visit(node)
        elif isinstance(node, ast.While):
            self.loops['While'] += 1
            nested_level = self.has_nested_loops(node)
            if nested_level > self.loops['nested While']:
                self.loops['nested While'] = nested_level
            self.generic_visit(node)
        else:
            node_type = type(node).__name__
            if node_type in self.operations:
                self.operations[node_type] += 1
            self.generic_visit(node)

    def has_nested_loops(self, node, level=0):
        if isinstance(node, ast.For) or isinstance(node, ast.While):
            max_level = level
            for child_node in ast.iter_child_nodes(node):
                max_level = max(max_level, self.has_nested_loops(child_node, level + 1))
            return max_level
        return level


def analyze_code_from_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
    tree = ast.parse(code)
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)
    return analyzer.operations, analyzer.loops


def print_asymptotic_notation(loops):
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


if __name__ == "__main__":
    file_path = "file.txt"
    operations, loops = analyze_code_from_file(file_path)

    print("Operations:")
    for op, count in operations.items():
        print(f"{op}: {count}")

    print("\nLoops:")
    for loop, count in loops.items():
        if "nested" in loop:
            print(f"{loop}: {count}")
        elif "For" in loop or "While" in loop:
            if CodeAnalyzer().has_nested_loops(loop):
                print(f"{loop}->nested {loop}: {count}")
            else:
                print(f"{loop}: {count}")

    print("\nAsymptotic Notation:")
    print_asymptotic_notation(loops)
