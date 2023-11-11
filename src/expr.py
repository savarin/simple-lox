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
    ...


@dataclasses.dataclass
class Name(Expr):
    text: str


@dataclasses.dataclass
class Call(Expr):
    callee: Name
    arguments: List[Expr]


@dataclasses.dataclass
class Integer(Expr):
    value: str


@dataclasses.dataclass
class Numeric(Expr):
    operator: Operator
    left: Expr
    right: Expr


@dataclasses.dataclass
class Relational(Expr):
    operator: Operator
    left: Expr
    right: Expr
