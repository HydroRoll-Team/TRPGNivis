from psi.lexer import Lexer, Token


__all__ = ['Parser']

class Parser:
    def __init__(self, input):
        self.lexer = Lexer(input)
        self.tokens = iter(self.lexer)
        self.current_token = next(self.tokens)

    def parse(self):
        return self.parse_expr()

    def parse_expr(self):
        token = self.current_token
        if token.value == '?':
            self.eat('?')

            condition = self.parse_condition()

            self.eat(':')

            if condition:
                result = self.parse_reply()
            else:
                result = None

            return result

    def parse_condition(self):
        variable = self.parse_variable()
        self.eat('==')
        value = self.parse_value()

        return variable == value

    def parse_variable(self):
        token = self.current_token
        self.eat('IDENTIFIER')
        return token.value

    def parse_value(self):
        token = self.current_token
        if token.type == 'INTEGER':
            self.eat('INTEGER')
            return token.value
        else:
            raise Exception(f'Invalid value: {token.value}')

    def parse_reply(self):
        self.eat('reply')
        self.eat(':')

        token = self.current_token
        if token.type != 'SEPARATOR':
            raise Exception(f'Invalid reply: {token.value}')

        return token.value

    def eat(self, expected_type):
        if self.current_token.type == expected_type:
            self.current_token = next(self.tokens)
        else:
            raise Exception(f'Unexpected token: {self.current_token.value}')
