from pprint import pprint
from abstract_syntax_tree import (
    Assignment,
    BinaryOperation,
    BinaryOperator,
    Block,
    Number,
    Print,
    Variable,
    While,
)
from interpreter import Interpreter


def main():
    program = Block(
        [
            Assignment(Variable("x"), Number(5)),
            While(
                BinaryOperation(
                    Variable("x"),
                    BinaryOperator.NOT_EQUALS,
                    Number(0),
                ),
                Block(
                    [
                        Print(Variable("x")),
                        Assignment(
                            Variable("x"),
                            BinaryOperation(
                                Variable("x"),
                                BinaryOperator.SUBTRACT,
                                Number(1),
                            ),
                        ),
                    ]
                ),
            ),
        ]
    )

    interpreter = Interpreter()
    interpreter.execute(program)
    print("\n\nFinal environment:")
    pprint(interpreter.get_environment())


if __name__ == "__main__":
    main()
