from psi.lexer import Token


__all__ = ['Interpreter']

class Interpreter:
    def __init__(self, ast):
        self.ast = ast

    def interpret(self):
        return self.interpret_expr(self.ast)

    def interpret_expr(self, node):
        if isinstance(node, Token):
            return node.value
        elif isinstance(node, list):
            for expr in node:
                result = self.interpret_expr(expr)
                if result is not None:
                    return result

    def interpret_condition(self, node):
        variable = self.interpret_expr(node[0])
        value = self.interpret_expr(node[2])

        return variable == value
