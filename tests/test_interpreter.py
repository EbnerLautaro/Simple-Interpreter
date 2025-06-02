from abstract_syntax_tree import (
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


def test_simple_assignment_and_print():
    """
    Pseudocode:
    ```
    x = 42
    print x
    ```
    """

    program = Block([Assignment(Variable("x"), Number(42)), Print(Variable("x"))])
    interpreter = Interpreter()
    interpreter.execute(program)

    enviroment = interpreter.get_environment()
    assert enviroment["x"] == 42


def test_arithmetic_expression():
    """
    Pseudocode:
    ```
    result = 10 + 5
    print result
    ```
    """
    program = Block(
        [
            Assignment(Variable("result"), BinaryOperation(Number(10), BinaryOperator.ADD, Number(5))),
            Print(Variable("result")),
        ]
    )
    interpreter = Interpreter()
    interpreter.execute(program)
    enviroment = interpreter.get_environment()
    assert enviroment["result"] == 15


def test_conditional_true():
    """
    Pseudocode:
    ```
    x = 5
    if x > 0:
        print 1
    else:
        print 0
    ```
    """
    program = Block(
        [
            Assignment(Variable("x"), Number(5)),
            If(
                BinaryOperation(Variable("x"), BinaryOperator.GT, Number(0)),
                then_branch=Block([Print(Number(1))]),
                else_branch=Block([Print(Number(0))]),
            ),
        ]
    )
    interpreter = Interpreter()
    interpreter.execute(program)
    enviroment = interpreter.get_environment()
    assert enviroment["x"] == 5


def test_while_loop():
    """
    Pseudocode:
    ```
    counter = 0
    while counter < 3:
        print counter
        counter = counter + 1
    ```
    """
    program = Block(
        [
            Assignment(Variable("counter"), Number(0)),
            While(
                BinaryOperation(Variable("counter"), BinaryOperator.LT, Number(3)),
                Block(
                    [
                        Print(Variable("counter")),
                        Assignment(
                            Variable("counter"), BinaryOperation(Variable("counter"), BinaryOperator.ADD, Number(1))
                        ),
                    ]
                ),
            ),
        ]
    )
    interpreter = Interpreter()
    interpreter.execute(program)
    enviroment = interpreter.get_environment()
    assert enviroment["counter"] == 3
