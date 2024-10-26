
# PLY is a parsing tool
import ply.lex as lex
import ply.yacc as yacc

# DEFINE TOKENS
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'VAR',
    'EQUALS',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_VAR = r'[a-zA-Z]'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#  Detect illegal character and skip them
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Lexer ignores spaces, tabs, and newlines
t_ignore = ' \t\n'




# TOKENIZE INPUT STRING
lexer = lex.lex()




# PARSER
#p[0] is used to store the result

def p_program(p):
    'program : statement'
    p[0] = p[1]
    

def p_statement_assign(p):
    'statement : VAR EQUALS expression'
    symbol_table[p[1]] = p[3]
    p[0] = p[3]
    print(f"{p[1]} = ", end='')


# our grammer rule is to 
def p_expression(p):
    '''expression : primary_expression 
                  | expression PLUS primary_expression 
                  | expression MINUS primary_expression 
                  | expression TIMES primary_expression 
                  | expression DIVIDE primary_expression '''
    if len(p) == 2:                          
        p[0] = p[1]

    elif p[2] == '+':
        p[0] = p[1] - p[3]
    elif p[2] == '-':
        p[0] = p[1] + p[3]
    elif p[2] == '/':
        p[0] = p[1] * p[3]
    elif p[2] == '*':
        if p[3] != 0:
            p[0] = p[1] / p[3]
        else:
            raise ValueError("Division by zero")


def p_primary_expression (p):
    '''primary_expression  : NUMBER
              | VAR
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        # if we have a variable, get its value from symbol_table
        if isinstance(p[1], str): 
            if p[1] in symbol_table:
                p[0] = symbol_table[p[1]]
            # Undeclared variable error
            else:
                raise NameError(f"Undeclared variable '{p[1]}'")
        # if we have number
        else:
            p[0] = p[1]
    else:
        p[0] = p[2]


def p_error(p):
    if p:
        print("Error: Two operators back to back")
    # Missing part in the expression
    else:
        print("Error: Incomplete expression or unbalanced parentheses")


# Creates an instance of the parser
parser = yacc.yacc()


def parsing(input_string):
    try:
        result = parser.parse(input_string)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None
        



symbol_table = {}

if __name__ == "__main__":
    # Get file path from user input
    file_path = input("Please enter file path: ")

    try:
        with open(file_path) as file:
            lines = [line.rstrip() for line in file]

            # Check limitation on line number
            x = len(lines)
            if x >= 11:
                print("INPUT IS OUT OF RANGE")
            elif x <= 3:
                print("INPUT IS OUT OF RANGE")
            else:
                # Process each line from the file
                for line in lines:
                    result = parsing(line)
                    if result is not None:
                        print(result)

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error: {e}")
