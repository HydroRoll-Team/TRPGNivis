from psi.parsers import Parser
from psi.interpreter import Interpreter

__all__ = ['Execution']

class Execution:
    def __init__(self, input):
        self.input = input

    def execute(self):
        parser = Parser(self.input)
        ast = parser.parse()

        interpreter = Interpreter(ast)
        result = interpreter.interpret()

        return result
