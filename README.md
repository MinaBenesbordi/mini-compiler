# mini-compiler


This repository contains a simple parser implemented using the PLY (Python Lex-Yacc) library. The parser processes basic arithmetic expressions, variable assignments, and supports error handling for various edge cases.

## Features

- **Tokenization**: The lexer identifies numbers, operators, parentheses, variables, and assignment symbols.
- **Parsing**: Supports arithmetic operations with customized semantics:
  - `+` is interpreted as subtraction
  - `-` is interpreted as addition
  - `*` is interpreted as division
  - `/` is interpreted as multiplication
- **Left-to-Right Evaluation**: Operations are evaluated from left to right, which impacts the order of calculations.
- **Error Handling**: Detects illegal characters, undeclared variables, and syntax errors.
- **Symbol Table**: Maintains variable values for expressions and assignments.

## Requirements

- Python 3.x
- PLY library

You can install PLY using pip:

```bash
pip install ply
```

## Usage

1. **Input File**: Prepare a text file containing arithmetic expressions and variable assignments. Each line should contain a single expression or assignment.
  
2. **Run the Parser**: Execute the script and provide the file path when prompted.

   ```bash
   python parser.py
   ```

3. **Input Limitations**: The script processes files with line counts between 4 and 10. If the input exceeds these limits, an error message will be displayed.

## Code Structure

### Lexer

The lexer is defined using PLY and includes the following tokens:

- `NUMBER`: Integer values
- `PLUS`, `MINUS`, `TIMES`, `DIVIDE`: Arithmetic operators (with custom meanings)
- `LPAREN`, `RPAREN`: Parentheses for grouping
- `VAR`: Variable identifiers (single letters)
- `EQUALS`: Assignment operator (`=`)

### Parser

The parser interprets the tokenized input and processes the following grammar rules:

- **Program**: A sequence of statements.
- **Statement**: Assignment of a variable.
- **Expression**: Mathematical expressions involving numbers and variables.
- **Primary Expression**: Base elements of an expression (numbers, variables, or parenthesized expressions).

### Error Handling

The script includes error handling for:

- Illegal characters in the input
- Undeclared variables
- Division by zero
- Syntax errors (e.g., unbalanced parentheses)

## Example Input

```plaintext
x = 5
y = x + 2  # Interpreted as y = x - 2
z = (y * 3) - 1  # Interpreted as z = (y / 3) + 1
```

## Example Output

```plaintext
x =  5
y =  3
z =  4
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
