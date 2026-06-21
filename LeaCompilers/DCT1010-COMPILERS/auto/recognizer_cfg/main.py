from typing import Optional, Self


class Node:
    def __init__(self, symbol: str, state: int, next: Optional[Self] = None):
        self.symbol = symbol
        self.state = state
        self.next = next


class DPA:
    def __init__(self, n: int, start: int, final: set, transitions: list[Node]):
        self.n = n
        self.start = start
        self.final = final
        self.transitions = transitions
        self.stack = []

    def make_transition(self, current_state: Optional[int], symbol: str):
        for transition in self.transitions:
            is_same_symbol = transition.symbol == symbol
            is_same_state = transition.state == current_state
            is_digit_symbol = transition.symbol == "digit" and symbol.isdigit()

            if (
                is_same_state
                and (is_same_symbol or is_digit_symbol)
                and transition.next is not None
            ):
                if transition.symbol == "(":
                    self.stack.append(symbol)
                elif transition.symbol == ")":
                    if len(self.stack) > 0:
                        self.stack.pop()
                    else:
                        return None

                return transition.next.state

        return None


class ExpressionCFGRecognizer:
    def __init__(self):
        self.auto = DPA(
            n=0,
            start=0,
            final={1, 2, 7},
            transitions=[
                # Recognize digits and $
                Node("digit", 0, Node("digit", 1)),
                Node("digit", 1, Node("digit", 1)),
                Node("$", 1, Node("$", 1)),
                # Recognize parentheses of expression
                Node("(", 0, Node("(", 2)),
                Node("(", 2, Node("(", 2)),
                # Recognize numbers recursively
                Node("digit", 2, Node("digit", 3)),
                Node("digit", 3, Node("digit", 3)),
                ##################### MAIN MACHINE
                Node("+", 3, Node("digit", 4)),
                Node("digit", 4, Node("digit", 5)),
                Node("(", 4, Node("digit", 2)),
                ##################### MAIN MACHINE
                Node("-", 3, Node("digit", 4)),
                Node("digit", 4, Node("digit", 5)),
                Node("(", 4, Node("digit", 2)),
                ##################### MAIN MACHINE
                Node("*", 3, Node("digit", 4)),
                Node("digit", 4, Node("digit", 5)),
                Node("(", 4, Node("digit", 2)),
                ##################### MAIN MACHINE
                Node("/", 3, Node("digit", 4)),
                Node("digit", 4, Node("digit", 5)),
                Node("(", 4, Node("digit", 2)),
                # Recognize numbers recursively
                Node("digit", 5, Node("digit", 5)),
                Node(")", 5, Node("digit", 6)),
                # Close parentheses recursively
                Node(")", 6, Node("digit", 6)),
                # Recognize new expressions
                Node("+", 6, Node("digit", 4)),
                Node("-", 6, Node("digit", 4)),
                Node("*", 6, Node("digit", 4)),
                Node("/", 6, Node("digit", 4)),
                # END
                Node("$", 6, Node("$", 7)),
            ],
        )

    def recognize_expression(self, expression: str) -> bool:
        state = self.auto.start

        for char in expression:
            if char == " ":
                continue

            state = self.auto.make_transition(state, char)

        return state in self.auto.final and len(self.auto.stack) == 0


def main():
    expression = "((17 + 91) - (67 * (15 / 5)))$"

    cfg_er = ExpressionCFGRecognizer()

    if cfg_er.recognize_expression(expression):
        print("A expressão é válida.")
    else:
        print("A expressão é inválida.")


if __name__ == "__main__":
    main()
