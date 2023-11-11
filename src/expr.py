"""
The expr.py module defines the classes representing expression nodes in the abstract syntax tree
(AST). These include basic constructs such as integers, names, and more complex ones like binary
operations and function calls.
"""

from typing import List
import dataclasses
import enum


class Operator(enum.Enum):
    EQUAL = "="
    GREATER = ">"
    LESS = "<"
    MINUS = "-"
    PLUS = "+"
    TIMES = "*"


class Expr:
    """
    The base class for expressions in the abstract syntax tree (AST).
    All specific expression types inherit from this class.
    """

    ...


@dataclasses.dataclass
class Name(Expr):
    """
    Represents a named identifier in the language.

    Attributes:
        text (str): The name of the identifier.
    """

    text: str


@dataclasses.dataclass
class Call(Expr):
    """
    Represents a function call in the language.

    Attributes:
        callee (Name): The name of the function being called.
        arguments (List[Expr]): A list of expressions representing the arguments passed to the function.
    """

    callee: Name
    arguments: List[Expr]


@dataclasses.dataclass
class Integer(Expr):
    """
    Represents an integer literal in the language.

    Attributes:
        value (str): The string representation of the integer value.
    """

    value: str


@dataclasses.dataclass
class Numeric(Expr):
    """
    Represents a numeric operation (like addition, subtraction) in the language.

    Attributes:
        operator (Operator): The operator used in the operation.
        left (Expr): The left operand of the operation.
        right (Expr): The right operand of the operation.
    """

    operator: Operator
    left: Expr
    right: Expr


@dataclasses.dataclass
class Relational(Expr):
    """
    Represents a relational operation (like equals, greater than, less than) in the language.

    Attributes:
        operator (Operator): The relational operator.
        left (Expr): The left operand of the relational operation.
        right (Expr): The right operand of the relational operation.
    """

    operator: Operator
    left: Expr
    right: Expr
