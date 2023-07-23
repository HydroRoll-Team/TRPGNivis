"""Psi
@TODO 词法分析器
@BODY 似乎要写的还蛮多的，所以先写几个TODO List
"""

__all__ = ['Psi']

from psi.execution import Execution

class Psi:
    def __init__(self, input):
        self.input = input
        self.execution = Execution(input)
        self.result = None

    def execute(self):
        self.result = self.execution.execute()
        return self.result

    def get_result(self):
        return self.result

    def set_input(self, input):
        self.input = input
        self.execution = Execution(input)
        self.result = None
