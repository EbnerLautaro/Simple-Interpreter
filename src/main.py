from abstract_syntax_tree import (
    ASTPrimitives,
    Assignment,
    Block,
    Number,
    Print,
    Variable,
)

from interpreter import Interpreter


def main():
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
