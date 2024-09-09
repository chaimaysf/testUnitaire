class RPNCalculator:
    def evaluate(self, expression):
        stack = []
        for token in expression.split():
            if token in "+-*":
                if len(stack) < 2:
                    raise ValueError("Not enough operands")
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
            else:
                try:
                    stack.append(int(token))
                except ValueError:
                    raise ValueError(f"Invalid token: {token}")
        if len(stack) != 1:
            raise ValueError("The expression is malformed")
        return stack[0]
