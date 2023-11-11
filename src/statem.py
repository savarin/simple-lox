"""
The statem.py module defines various statement classes used in the abstract syntax tree (AST). This
includes statements like variable declarations, control flow statements (if, else), function
definitions, and return statements.
"""

from typing import List, Optional
import dataclasses

import expr


class Statem:
    """
    The base class for statements in the abstract syntax tree (AST).
    All specific statement types inherit from this class.
    """

    ...


@dataclasses.dataclass
class Block(Statem):
    """
    Represents a block of statements, typically enclosed in braces.

    Attributes:
        statements (List[Statem]): A list of statement objects contained in the block.
    """

    statements: List[Statem]


@dataclasses.dataclass
class Expression(Statem):
    """
    Represents an expression statement in the language.

    Attributes:
        expression (Expr): The expression that constitutes this statement.
    """

    expression: expr.Expr


@dataclasses.dataclass
class Function(Statem):
    """
    Represents a function definition in the language.

    Attributes:
        name (expr.Name): The name of the function.
        parameters (List[expr.Name]): A list of parameters (names) for the function.
        body (Block): The body of the function, consisting of a sequence of statements.
    """

    name: expr.Name
    parameters: List[expr.Name]
    body: Block


@dataclasses.dataclass
class If(Statem):
    """
    Represents an 'if' conditional statement in the language.

    Attributes:
        condition (expr.Expr): The expression evaluated to determine the branch to execute.
        then_branch (Block): The block of statements executed if the condition is true.
        else_branch (Optional[Block]): The block of statements executed if the condition is false, can be None.
    """

    condition: expr.Expr
    then_branch: Block
    else_branch: Optional[Block]


@dataclasses.dataclass
class Variable(Statem):
    """
    Represents a variable declaration in the language.

    Attributes:
        name (expr.Name): The name of the variable being declared.
        initializer (expr.Expr): The expression used to initialize the variable.
    """

    name: expr.Name
    initializer: expr.Expr


@dataclasses.dataclass
class Return(Statem):
    """
    Represents a return statement in a function.

    Attributes:
        expression (expr.Expr): The expression whose value is returned by the statement.
    """

    expression: expr.Expr
