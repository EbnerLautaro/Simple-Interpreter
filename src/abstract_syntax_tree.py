from abc import ABC
from enum import Enum
from typing import Optional


class UnaryOperator(Enum):
    """
    Enum representing the types of unary operators in an expression.
    """

    # Arithmetic operators
    MINUS = "MINUS"
    # # Logical operators
    NOT = "NOT"


class BinaryOperator(Enum):
    """
    Enum representing the types of binary operators in an expression.
    """

    # Arithmetic operators
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    GT = "GT"
    LT = "LT"
    GTE = "GTE"
    LTE = "LTE"
    # Logical operators
    AND = "AND"
    OR = "OR"
    # Others
    ASSIGN = "ASSIGN"


ASTPrimitives = bool | int | float
# --------------------------------------------------------------------------------------------


class ASTNode(ABC):
    """
    Base class for all nodes in the abstract syntax tree.
    """

    pass


# --------------------------------------------------------------------------------------------


class Expression(ASTNode):
    """
    Base class for all expressions in the abstract syntax tree.
    """

    pass


class Number(Expression):
    """
    Represents a numeric literal in the abstract syntax tree.
    """

    def __init__(self, value: float):
        self.value = value


class Boolean(Expression):
    """
    Represents a boolean literal in the abstract syntax tree.
    """

    def __init__(self, value: bool):
        self.value = value


class Variable(Expression):
    """
    Represents a variable in the abstract syntax tree.
    """

    def __init__(self, name: str):
        self.name = name


class BinaryOperation(Expression):
    """
    Represents a binary operation in the abstract syntax tree.
    """

    def __init__(self, left: Expression, operator: BinaryOperator, right: Expression):
        self.left = left
        self.operator = operator
        self.right = right


class UnaryOperation(Expression):
    """
    Represents a unary operation in the abstract syntax tree.
    """

    def __init__(self, operator: UnaryOperator, operand: Expression):
        self.operator = operator
        self.operand = operand


# --------------------------------------------------------------------------------------------


class Command(ASTNode):
    """
    Base class for all commands in the abstract syntax tree.
    """

    pass


class Assignment(Command):
    """
    Represents an assignment operation in the abstract syntax tree.
    """

    def __init__(self, variable: Variable, value: Expression):
        self.variable = variable
        self.value = value


class Block(Command):
    """
    Represents a sequence of statements in the abstract syntax tree.
    """

    def __init__(self, statements: list[Command]):
        self.statements = statements


class If(Command):
    """
    Represents an if statement in the abstract syntax tree.
    """

    def __init__(self, condition: Expression, then_branch: Block, else_branch: Optional[Block] = None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch


class While(Command):
    """
    Represents a while loop in the abstract syntax tree.
    """

    def __init__(self, condition: Expression, body: Block):
        self.condition = condition
        self.body = body


class Print(Command):
    """
    Represents a print command in the abstract syntax tree.
    """

    def __init__(self, expression: Expression):
        self.expression = expression
