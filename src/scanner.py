"""
The scanner.py module, also known as the lexer, is responsible for breaking down the source code
text into a sequence of tokens. These tokens represent the syntactic elements like keywords,
operators, literals, and identifiers, which are then used by the parser.py module to create the AST.
"""

from typing import Dict, List
import dataclasses
import enum


class TokenType(enum.Enum):
    # Types
    INTEGER = "INTEGER"

    # Names
    NAME = "NAME"

    # Single-character tokens.
    BRACE_LEFT = "BRACE_LEFT"
    BRACE_RIGHT = "BRACE_RIGHT"
    COMMA = "COMMA"
    EQUAL = "EQUAL"
    GREATER = "GREATER"
    LESS = "LESS"
    MINUS = "MINUS"
    PAREN_LEFT = "PAREN_LEFT"
    PAREN_RIGHT = "PAREN_RIGHT"
    PLUS = "PLUS"
    SEMICOLON = "SEMICOLON"
    TIMES = "TIMES"

    # Keywords
    FUNC = "FUNC"
    ELSE = "ELSE"
    IF = "IF"
    RETURN = "RETURN"
    VAR = "VAR"

    EOF = "EOF"


LITERALS: Dict[str, TokenType] = {
    "{": TokenType.BRACE_LEFT,
    "}": TokenType.BRACE_RIGHT,
    ",": TokenType.COMMA,
    "=": TokenType.EQUAL,
    ">": TokenType.GREATER,
    "<": TokenType.LESS,
    "-": TokenType.MINUS,
    "(": TokenType.PAREN_LEFT,
    ")": TokenType.PAREN_RIGHT,
    "+": TokenType.PLUS,
    ";": TokenType.SEMICOLON,
    "*": TokenType.TIMES,
}


KEYWORDS: Dict[str, TokenType] = {
    "func": TokenType.FUNC,
    "else": TokenType.ELSE,
    "if": TokenType.IF,
    "return": TokenType.RETURN,
    "var": TokenType.VAR,
}


@dataclasses.dataclass
class Token:
    """
    Represents a lexical token with a specific type, value, and line number.

    Attributes:
        token_type (TokenType): The type of the token (e.g., INTEGER, NAME).
        value (str): The string value of the token.
        line (int): The line number in the source code where the token appears.
    """

    token_type: TokenType
    value: str
    line: int


def scan(source: str) -> List[Token]:
    """
    Converts source code text into a list of tokens, representing syntactic elements like
    keywords, operators, literals, and identifiers.

    Args:
        source (str): The source code to tokenize.

    Returns:
        List[Token]: The list of tokens extracted from the source code.

    Raises:
        Exception: If an unrecognized character is encountered in the source.
    """
    tokens: List[Token] = []
    counter: int = 0
    line: int = 1

    while counter < len(source):
        # Line numbers.
        if source[counter] == "\n":
            counter += 1
            line += 1

        # Whitespace
        elif source[counter].isspace():
            counter += 1

        # Names
        elif source[counter].isalpha():
            start = counter

            while counter < len(source) and source[counter].isalpha():
                counter += 1

            name = source[start:counter]
            token_type = KEYWORDS.get(name, TokenType.NAME)

            tokens.append(Token(token_type, name, line))

        # Integers
        elif source[counter].isdigit():
            start = counter

            while counter < len(source) and source[counter].isdigit():
                counter += 1

            tokens.append(Token(TokenType.INTEGER, source[start:counter], line))

        # Literals
        elif source[counter] in LITERALS:
            tokens.append(Token(LITERALS[source[counter]], source[counter], line))
            counter += 1

        else:
            raise SyntaxError(
                f"Unrecognized character '{source[counter]}' at position {counter}, line {line}."
            )

    return tokens + [Token(TokenType.EOF, "EOF", line)]
