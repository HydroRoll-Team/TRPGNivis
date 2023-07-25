class AssignNode:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

class ComparisonNode:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

class IfNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ReplyNode:
    def __init__(self, message):
        self.message = message

import ast

def parse_code(code):
    tree = ast.parse(code)
    return parse_node(tree.body[0])

def parse_node(node):
    if isinstance(node, ast.Assign):
        variable = node.targets[0].id
        value = parse_node(node.value)
        return AssignNode(variable, value)
    elif isinstance(node, ast.Compare):
        operator = node.ops[0]
        left = parse_node(node.left)
        right = parse_node(node.comparators[0])
        return ComparisonNode(operator, left, right)
    elif isinstance(node, ast.If):
        condition = parse_node(node.test)
        body = parse_node(node.body[0])
        return IfNode(condition, body)
    elif isinstance(node, ast.Expr):
        return ReplyNode(node.value.s)
    elif isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Num):
        return node.n

def execute_ast(ast, environment):
    if isinstance(ast, AssignNode):
        environment[ast.variable] = ast.value
    elif isinstance(ast, ComparisonNode):
        left = execute_ast(ast.left, environment)
        right = execute_ast(ast.right, environment)
        if ast.operator == '==':
            return left == right
        elif ast.operator == '!=':
            return left != right
        elif ast.operator == '<':
            return left < right
        elif ast.operator == '>':
            return left > right
    elif isinstance(ast, IfNode):
        condition = execute_ast(ast.condition, environment)
        if condition:
            execute_ast(ast.body, environment)
    elif isinstance(ast, ReplyNode):
        message = ast.message.format(**environment)
        print(message)

def main():
    code = input("请输入代码: ")
    ast = parse_code(code)
    environment = {}
    execute_ast(ast, environment)

if __name__ == "__main__":
    main()
