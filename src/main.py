from abstract_syntax_tree import (
    ASTPrimitives,
    Assignment,
    BinaryOperation,
    BinaryOperator,
    Block,
    If,
    Number,
    Print,
    Variable,
    While,
)

from interpreter import Interpreter


def main():
    """
    Dejo este archivo como una entrada rapida y sencilla para ejecutar programas.
    Para ejemplos ya creados se puede ver la carpeta de `tests` (por simplicidad solo se incluyeron tests del interprete).
    """

    program = Block(
        [
            Print(Variable("x")),
            Assignment(Variable("x"), Number(5)),
            Print(Variable("x")),
        ]
    )

    initial_environment: dict[str, ASTPrimitives] = {"x": 100_000}

    interpreter = Interpreter(context=initial_environment)
    interpreter.execute(program=program, allow_output=True)

    print("Environment after execution:")
    print(interpreter.get_environment())


if __name__ == "__main__":
    main()
