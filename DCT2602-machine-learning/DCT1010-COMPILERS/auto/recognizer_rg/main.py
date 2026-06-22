from typing import Optional, Self


class Node:
    def __init__(self, symbol: str, state: int, next: Optional[Self] = None):
        self.symbol = symbol
        self.state = state
        self.next = next


class DFA:
    def __init__(self, n: int, start: int, final: set, transitions: list[Node]):
        self.n = n
        self.start = start
        self.final = final
        self.transitions = transitions

    def make_transition(
        self, current_state: Optional[int], symbol: str
    ) -> Optional[int]:
        for transition in self.transitions:
            is_same_symbol = transition.symbol == symbol
            is_same_state = transition.state == current_state
            is_digit_symbol = transition.symbol == "digit" and symbol.isdigit()

            if (
                is_same_state
                and (is_same_symbol or is_digit_symbol)
                and transition.next is not None
            ):
                return transition.next.state

        return None


class ExpressionRecognizer:
    def __init__(self):
        self.dfa = DFA(
            n=8,
            start=0,
            final={3},
            transitions=[
                # Start
                Node("digit", 0, Node("digit", 1)),
                # Recognize numbers recursively
                Node("digit", 1, Node("digit", 1)),
                # Recognize operators
                Node("+", 1, Node("digit", 2)),
                Node("-", 1, Node("digit", 2)),
                Node("*", 1, Node("digit", 2)),
                Node("/", 1, Node("digit", 2)),
                # Recognize number and return to 1 state
                Node("digit", 2, Node("digit", 1)),
                # END
                Node("$", 1, Node("$", 3)),
            ],
        )

    def recognize_expression(self, expression: str) -> bool:
        state = self.dfa.start

        for char in expression:
            if char == " ":
                continue

            state = self.dfa.make_transition(state, char)

        return state in self.dfa.final


def main():
    expression = "17 + 91 - 67 * 15 / 5$"

    rg_er = ExpressionRecognizer()

    if rg_er.recognize_expression(expression):
        print("A expressão é válida.")
    else:
        print("A expressão é inválida.")


if __name__ == "__main__":
    main()
