# simple-lox

`simple-lox` is an implementation of the [Lox programming language](https://craftinginterpreters.com/the-lox-language.html). Designed to be both efficient and easy to understand, it serves as a practical example of language design and interpreter implementation.

## Context

Lox is a high-level programming language introduced in the book [Crafting Interpreters](https://craftinginterpreters.com/contents.html). It is commonly used for educational purposes to illustrate key concepts in language design, parsing, and interpretation. This implementation of Lox in Python showcases a balance between readability and functionality, making it an ideal resource for those learning about compilers and interpreters.

## Features

- **Language Constructs**: Supports a variety of constructs including arithmetic operations, control flow statements, variables, and functions.
- **Parser Implementation**: Utilizes a recursive descent parser for syntax analysis, providing clear and maintainable code structure.
- **Interpreter Design**: Implements an abstract syntax tree (AST) interpreter, capable of executing Lox programs with high efficiency.
- **Error Handling**: Robust error handling mechanisms for syntax and runtime errors, ensuring clear feedback for debugging.
- **Extensibility**: Designed with extensibility in mind, allowing for easy addition of new language features or optimizations.

## Components

- **Expr Module (`expr.py`)**: Defines classes for expression nodes in the AST, including basic and complex constructs like binary operations and function calls.
- **Statem Module (`statem.py`)**: Contains classes for different types of statements in the Lox language, aiding in structuring the AST.
- **Scanner Module (`scanner.py`)**: Tokenizes the raw source code into a series of syntactic tokens, laying the foundation for parsing.
- **Parser Module (`parser.py`)**: Transforms tokens into an AST, employing a recursive descent parsing approach.
- **Interpreter Module (`interpreter.py`)**: Interprets the AST, executing the Lox program and managing the runtime environment.
- **Formatter Module (`formatter.py`)**: Provides functionality to convert AST nodes back into a readable string format, useful for debugging.

## Usage and Examples

To use `simple-lox`, follow these steps:
1. Clone the repository: `git clone git@github.com:savarin/simple-lox.git`.
2. Run the interpreter: `python run.py`.

Example:
```lox
// Fibonacci sequence in Lox
func fibonacci(n) {
  if (n < 2) {
    return n;
  }
  return fibonacci(n - 1) + fibonacci(n - 2);
}

print(fibonacci(9));
```

## Testing

The project includes a comprehensive suite of unit tests to ensure the correctness and stability of the implementation. Tests cover various aspects of language features, from basic expressions to complex function calls.

## Contributing

Contributions to `simple-lox` are welcome! Please refer to the contribution guidelines for details on submitting pull requests, reporting issues, or suggesting enhancements.
