from abstract_syntax_tree import (
    ASTPrimitives,
    Assignment,
    BinaryOperation,
    BinaryOperator,
    Block,
    Boolean,
    Command,
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

    def __init__(self, context: dict[str, ASTPrimitives] | None = None):
        """
        Initializes a new instance of the Interpreter class with an empty or partial environment.
        """
        self.context: dict[str, ASTPrimitives]
        self._environment = context if context is not None else {}

    def _evaluate_expression(self, node: Expression) -> ASTPrimitives:
        """
        Evaluates an expression node and returns its value.

        Raises:
            NameError: If a variable is undefined.
            NotImplementedError: If the operator is not implemented.
            TypeError: If the node type is not an expression.
        """

        if isinstance(node, Number):
            return node.value

        elif isinstance(node, Boolean):
            return bool(node.value)

        elif isinstance(node, Variable):
            if node.name in self._environment:
                return self._environment[node.name]
            raise NameError(f"Undefined variable: {node.name}")

        elif isinstance(node, UnaryOperation):
            operand = self._evaluate_expression(node.operand)
            if node.operator == UnaryOperator.MINUS:
                return -operand
            if node.operator == UnaryOperator.NOT:
                return not operand

            raise NotImplementedError(f"Unary operator {node.operator} not implemented")

        elif isinstance(node, BinaryOperation):
            left = self._evaluate_expression(node.left)
            right = self._evaluate_expression(node.right)

            if node.operator == BinaryOperator.ADD:
                return left + right
            elif node.operator == BinaryOperator.SUBTRACT:
                return left - right
            elif node.operator == BinaryOperator.MULTIPLY:
                return left * right
            elif node.operator == BinaryOperator.DIVIDE:
                return left / right
            elif node.operator == BinaryOperator.EQUALS:
                return left == right
            elif node.operator == BinaryOperator.AND:
                return left and right
            elif node.operator == BinaryOperator.OR:
                return left or right
            elif node.operator == BinaryOperator.NOT_EQUALS:
                return left != right
            elif node.operator == BinaryOperator.GT:
                return left > right
            elif node.operator == BinaryOperator.LT:
                return left < right
            elif node.operator == BinaryOperator.GTE:
                return left >= right
            elif node.operator == BinaryOperator.LTE:
                return left <= right
            elif node.operator == BinaryOperator.ASSIGN:
                if isinstance(node.left, Variable):
                    value = self._evaluate_expression(node.right)
                    self._environment[node.left.name] = value
                    return value

                raise SyntaxError("Left-hand side of assignment must be a variable")

            else:
                raise NotImplementedError(f"Binary operator {node.operator} not implemented")

        else:
            raise TypeError(f"Unexpected node type: {type(node)}")

    def _execute_command(self, command: Command, allow_output: bool):
        """
        Executes a command node.

        Raises:
            TypeError: If the command type is unrecognized.
        """
        if isinstance(command, Assignment):
            value = self._evaluate_expression(command.value)
            self._environment[command.variable.name] = value

        elif isinstance(command, Print):
            if allow_output:
                value = self._evaluate_expression(command.expression)
                print(value)

        elif isinstance(command, Block):
            for statement in command.statements:
                self._execute_command(statement, allow_output)

        elif isinstance(command, If):
            condition = self._evaluate_expression(command.condition)
            if condition:
                self._execute_command(command.then_branch, allow_output)
            if not condition and command.else_branch is not None:
                self._execute_command(command.else_branch, allow_output)

        elif isinstance(command, While):
            condition = self._evaluate_expression(command.condition)

            while condition:
                self._execute_command(command.body, allow_output)
                condition = self._evaluate_expression(command.condition)

        else:
            raise TypeError(f"Unexpected command type: {type(command)}")

    def execute(self, program: Block, allow_output: bool = True):
        """
        Executes a program represented as a Block of commands.

        Args:
            program (Block): The program to execute.
        """
        self._execute_command(program, allow_output)

    def get_environment(self) -> dict:
        """
        Returns the current environment of the interpreter.
        """
        return self._environment
