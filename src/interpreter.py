from pprint import pprint
from abstract_syntax_tree import (
    ASTNode,
    Assignment,
    BinaryOperation,
    BinaryOperator,
    Block,
    Command,
    Exit,
    Expression,
    If,
    Number,
    Print,
    UnaryOperation,
    UnaryOperator,
    Variable,
    While,
)


class Interpreter:
    """
    Represents an interpreter for evaluating and executing an abstract syntax tree (AST).
    """

    def __init__(self):
        """
        Initializes a new instance of the Interpreter class with an empty environment.
        """
        self.environment = {}

    def get_environment(self) -> dict:
        """
        Returns the current environment of the interpreter.
        """
        return self.environment

    def evaluate_expression(self, node: Expression):
        """
        Evaluates an expression node and returns its value.

        Raises:
            NameError: If a variable is undefined.
            NotImplementedError: If the operator is not implemented.
            TypeError: If the node type is not an expression.
        """

        if isinstance(node, Number):
            return node.value

        elif isinstance(node, Variable):
            if node.name in self.environment:
                return self.environment[node.name]
            raise NameError(f"Undefined variable: {node.name}")

        elif isinstance(node, UnaryOperation):
            operand = self.evaluate_expression(node.operand)
            if node.operator == UnaryOperator.MINUS:
                return -operand

            raise NotImplementedError(f"Unary operator {node.operator} not implemented")

        elif isinstance(node, BinaryOperation):
            left = self.evaluate_expression(node.left)
            right = self.evaluate_expression(node.right)

            if node.operator == BinaryOperator.ADD:
                return left + right

            elif node.operator == BinaryOperator.SUBTRACT:
                return left - right

            elif node.operator == BinaryOperator.MULTIPLY:
                return left * right

            elif node.operator == BinaryOperator.DIVIDE:
                return left / right

            elif node.operator == BinaryOperator.EQUAL:
                return left == right

            elif node.operator == BinaryOperator.ASSIGN:
                if isinstance(node.left, Variable):
                    value = self.evaluate_expression(node.right)
                    self.environment[node.left.name] = value
                    return value

                raise SyntaxError("Left-hand side of assignment must be a variable")

            else:
                raise NotImplementedError(f"Binary operator {node.operator} not implemented")

        else:
            raise TypeError(f"Unexpected node type: {type(node)}")

    def execute_command(self, command: Command):
        """
        Executes a command node.

        Raises:
            SystemExit: If an Exit command is encountered.
            TypeError: If the command type is unrecognized.
        """
        if isinstance(command, Assignment):
            value = self.evaluate_expression(command.value)
            self.environment[command.variable.name] = value

        elif isinstance(command, Print):
            value = self.evaluate_expression(command.expression)
            print(value)

        elif isinstance(command, Exit):
            print("Exiting the program.")
            print("-" * 20, " Final environment ", "-" * 20)
            pprint(self.environment)
            print("-" * 60)
            raise SystemExit()

        elif isinstance(command, Block):
            for statement in command.statements:
                self.execute_command(statement)

        elif isinstance(command, If):
            condition = self.evaluate_expression(command.condition)
            if condition:
                self.execute_command(command.then_branch)

            elif command.else_branch is not None:
                self.execute_command(command.else_branch)

        elif isinstance(command, While):
            while self.evaluate_expression(command.condition):
                self.execute_command(command.body)

        else:
            raise TypeError(f"Unexpected command type: {type(command)}")
