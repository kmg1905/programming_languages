# Mukesh Goud Kondeti
# 112689870

import sys
import warnings
warnings.simplefilter("ignore", category = FutureWarning)

from ply import lex
from ply import yacc
import sys

# Exception classes

class SyntaxError(Exception):
    pass

class SemanticError(Exception):
    pass

# AST element class definitions
class Node:
    def __init__(self):
        pass

    def evaluate(self):
        return 0

class NodeBoolean(Node):
    def __init__(self, value):
        if value == 'False':
            self.value = False
        else:
            self.value = True

    def returnValue(self):
        return self.value

    def evaluate(self):
        return returnValue()


class NodeNumber(Node):
    def __init__(self, value):
        if ('.'  in value):
            self.value = float(value)
        else:
            self.value = int(value)

    def returnValue(self):
        return self.value

    def evaluate(self):
        return returnValue()

class NodeList(Node):
    def __init__(self, value):
        self.value = value

    def returnValue(self):
        return self.value

    def evaluate(self):
        return returnValue()


class NodeString(Node):
    def __init__(self, string):
        if remove:
            self.value = string[1:-1]
        else:
            self.value = string

    def returnValue(self):
        return self.value

    def evaluate(self):
        return returnValue()


class NodeTuple(Node):
    def __init__(self, value):
        self.value = value

    def returnValue(self):
        return self.value

    def evaluate(self):
        return returnValue()

# tuple of token names.
tokens = (
    'EQUAL', 'NOTEQUAL', 'GREATERTHAN', 'GREATEREQUAL', 'LESSERTHAN', 'LESSEREQUAL',
    'NUMBER',
    'EXPONENT', 'CONCAT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LEFTBRACKET', 'RIGHTBRACKET',
    'LEFTPARENTHESIS', 'RIGHTPARENTHESIS',
    'ANDALSO', 'ORELSE',
    'COMMA', 'TUPLE_INDEX',
    'INTDIV', 'MOD', 'IN', 'NOT',
    'STRING', 'BOOLEAN'
)

# dictioanry of Reserved words
reserved = {
    'and' : 'AND',
    'or'  : 'OR',
    'True': 'TRUE',
    'False': 'FALSE',
    'not' : 'NOT',
    'in'  : 'IN',
    'orelse': 'ORELSE',
    'andalso': 'ANDALSO',
    'mod': 'MOD',
    'div': 'DIV'
}

# Regular expression matching
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPONENT = r'\*\*'
t_CONCAT = r'\:\:'
t_LEFTPARENTHESIS = r'\('
t_RIGHTPARENTHESIS = r'\)'
t_LEFTBRACKET = r'\['
t_RIGHTBRACKET = r'\]'
t_COMMA = r'\,'
t_TUPLE_INDEX = r'\#'
t_INTDIV = r'div'
t_MOD = r'mod'
t_IN = r'in'
t_NOT = r'not'
t_EQUAL = r'=='
t_NOTEQUAL = r'\<\>'
t_GREATERTHAN = r'\>'
t_GREATEREQUAL = r'\>\='
t_LESSERTHAN = r'\<'
t_LESSEREQUAL = r'\<\='
t_ANDALSO = r'andalso'
t_ORELSE = r'orelse'



def t_NUMBER(t):
    r'\d*(\d\.|\.\d)\d*([eE]-?\d+)?|\d+'
    if '.' not in t.value:
        t.value = int(t.value)
    else:
        t.value = float(t.value)
    return t

def tokenize(inp):
    lexer.input(inp)
    while True:
        tok = lexer.token()
        if not tok:
            break


def t_BOOLEAN(t):
    r'False|True'
    if t.value == 'False':
        t.value = False
    elif t.value == 'True':
        t.value = True
    return t

def t_STRING(t):
    r'(\'(\\\n|\\\\|\\\"|\\\'|\\\t|[^\\\'])*\')|(\"(\\\n|\\\\|\\\"|\\\'|\\\t|[^\\\"])*\")'
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")



t_ignore = ' \t'


def t_error(t):
    print("Illegal Character '%s', at %d, %d" %
          (t.value[0], t.lineno, t.lexpos))
    t.lexer.skip(1)

# Precedence tuples
precedence = (
    ('right', 'EXPONENT'),
    ('left', 'LEFTBRACKET'), 
    ('left', 'RIGHTBRACKET'),
    ('left', 'TUPLE_INDEX'),
    ('left', 'IN'),
    ('left', 'PLUS'), 
    ('left', 'MINUS'),
    ('left', 'TIMES'), 
    ('left', 'DIVIDE'), 
    ('left', 'INTDIV'), 
    ('left', 'MOD'),
    ('left', 'LEFTPARENTHESIS'), 
    ('left','RIGHTPARENTHESIS'),
    ('left', 'ORELSE'),
    ('left', 'ANDALSO'),
    ('left', 'NOT'),
    ('left', 'LESSERTHAN'), 
    ('left', 'LESSEREQUAL'), 
    ('left', 'EQUAL'), 
    ('left', 'NOTEQUAL'), 
    ('left', 'GREATEREQUAL'), 
    ('left', 'GREATERTHAN'),
    ('right', 'CONCAT')
)

def p_block(p):
    'block : definition'
    value1 = p[1]
    same_type = None
    p[0] = value1

def p_multiply(p):
    'phase : definition TIMES definition'
    value1 = p[1]
    value2 = p[3]
    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    
    if not isinstance(value1, int) and not isinstance(value1, float):
        raise SemanticError()
    if not isinstance(value2, int) and not isinstance(value2, float):
        raise SemanticError()
    p[0] = value1 * value2

def p_summation(p):
    'definition : definition PLUS definition'

    value1 = p[1]
    value2 = p[3]
    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if same_type:
        raise SemanticError("Operands given are not of same type")

    if isinstance(value1, int) or isinstance(value1, float):
        if not isinstance(value2, int) and not isinstance(value2, float):
            raise SemanticError()
    elif not isinstance(value1, str) or not isinstance(value1, list):
        if type(value1) != type(value2):
            raise SemanticError()
    p[0] = p[1] + p[3]

def p_difference(p):
    'definition : definition MINUS definition'
    value1 = p[1]
    value2 = p[3]
    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    
    if not isinstance(value1, int) and not isinstance(value1, float):
        raise SemanticError()
    if not isinstance(value2, int) and not isinstance(value2, float):
        raise SemanticError()
    p[0] = value1 - value2

def p_division(p):
    'phase : definition DIVIDE definition'
    value1 = p[1]
    value2 = p[3]
    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    
    if not isinstance(value1, int) and not isinstance(value1, float):
        raise SemanticError()
    if not isinstance(value2, int) and not isinstance(value2, float):
        raise SemanticError()
    
    if value2 == 0:
        raise SemanticError()
    p[0] = value1 / value2

def p_division_floor(p):
    'definition : definition INTDIV definition'
    value1 = p[1]
    value2 = p[3]
    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    
    if not isinstance(value1, int) and not isinstance(value1, float):
        raise SemanticError()
    if not isinstance(value2, int) and not isinstance(value2, float):
        raise SemanticError()
    
    if value2 == 0:
        raise SemanticError()
    p[0] = value1 // value2

def p_modulus(p):
    'definition : definition MOD definition'
    value1 = p[1]
    value2 = p[3]
    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    
    if not isinstance(value1, int) and not isinstance(value1, float):
        raise SemanticError()
    if not isinstance(value2, int) and not isinstance(value2, float):
        raise SemanticError()
    
    if value2 == 0:
        raise SemanticError()
    p[0] = value1 % value2


def p_exponent(p):
    'definition : definition EXPONENT definition'
    value1 = p[1]
    value2 = p[3]
    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    
    if not isinstance(value1, int) and not isinstance(value1, float):
        raise SemanticError()
    if not isinstance(value2, int) and not isinstance(value2, float):
        raise SemanticError()
    p[0] = value1 ** value2

def p_merge(p):
    'definition : definition CONCAT definition'
    value1 = p[1]
    value2 = p[3]

    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    if not isinstance(value2, list):
        raise SemanticError()
    value2.insert(0, value1)
    p[0] = value2


def p_membershipIn(p):
    'definition : definition IN definition'
    value2 = p[1]
    value1 = p[3]

    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    if not isinstance(value1, str) and not isinstance(value1, list):
        raise SemanticError()

    p[0] = value2 in value1

def p_conjunction(p):
    'definition : definition ANDALSO definition'

    value1 = p[1]
    value2 = p[3]

    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    if not isinstance(value1, bool) or not isinstance(value2, bool):
        raise SemanticError()
    p[0] = value1 and value2



def p_negate(p):
    'definition : NOT definition'

    value2 = p[2]
    if not isinstance(value2, bool):
        raise SemanticError()
    p[0] = not value2



def p_disjunction(p):
    'definition : definition ORELSE definition'
    value1 = p[1]
    value2 = p[3]

    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    if not isinstance(value1, bool) or not isinstance(value2, bool):
        raise SemanticError()
    p[0] = value1 or value2

def p_not_equal(p):
    'definition : definition NOTEQUAL definition'
    value1 = p[1]
    value2 = p[3]

    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    if isinstance(value1, int) or isinstance(value1, float):
        if not isinstance(value2, int) and not isinstance(value2, float):
            raise SemanticError()
    if isinstance(value1, str)  or isinstance(value2, str) :
        if type(value1) != type(value2):
            raise SemanticError()
    p[0] = value1 != value2

def p_lesserthan(p):
    'definition : definition LESSERTHAN definition'

    value1 = p[1]
    value2 = p[3]

    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    if isinstance(value1, int) or isinstance(value1, float):
        if not isinstance(value2, int) and not isinstance(value2, float):
            raise SemanticError()
    if isinstance(value1, str)  or isinstance(value2, str) :
        if type(value1) != type(value2):
            raise SemanticError()
    p[0] = value1 < value2

def p_equal_equal(p):
    'definition : definition EQUAL definition'
    value1 = p[1]
    value2 = p[3]

    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    if isinstance(value1, int) or isinstance(value1, float):
        if not isinstance(value2, int) and not isinstance(value2, float):
            raise SemanticError()
    if isinstance(value1, str)  or isinstance(value2, str) :
        if type(value1) != type(value2):
            raise SemanticError()
    p[0] = value1 == value2

def p_lessthanequalto(p):
    'definition : definition LESSEREQUAL definition'

    value1 = p[1]
    value2 = p[3]

    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    if isinstance(value1, int) or isinstance(value1, float):
        if not isinstance(value2, int) and not isinstance(value2, float):
            raise SemanticError()
    if isinstance(value1, str)  or isinstance(value2, str) :
        if type(value1) != type(value2):
            raise SemanticError()
    p[0] = value1 <= value2

def p_greater_than(p):
    'definition : definition GREATERTHAN definition'
    value1 = p[1]
    value2 = p[3]

    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    if isinstance(value1, int) or isinstance(value1, float):
        if not isinstance(value2, int) and not isinstance(value2, float):
            raise SemanticError()
    if isinstance(value1, str)  or isinstance(value2, str) :
        if type(value1) != type(value2):
            raise SemanticError()
    p[0] = value1 > value2


def p_greater_than_or_equal(p):
    'definition : definition GREATEREQUAL definition'
    value1 = p[1]
    value2 = p[3]

    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__

    if False:
        raise SemanticError("Operands given are not of same type")
    if isinstance(value1, int) or isinstance(value1, float):
        if not isinstance(value2, int) and not isinstance(value2, float):
            raise SemanticError()
    if isinstance(value1, str)  or isinstance(value2, str) :
        if type(value1) != type(value2):
            raise SemanticError()
    p[0] = value1 >= value2


def p_list(p):
    'definition : LEFTBRACKET list_inside RIGHTBRACKET'

    value2 = p[2]
    p[0] = value2


def p_definition(p):
    'part : LEFTPARENTHESIS definition RIGHTPARENTHESIS'
    value2 = p[2]
    p[0] = value2

def p_list_inside_two(p):
    'list_inside : definition'
    value1 = p[1]
    p[0] = [value1]


def p_list_inside(p):
    'list_inside : definition COMMA list_inside'
    value2 = p[3]
    value1 = p[1]

    p[0] = [value1] + value2

def p_list_index_define(p):
    'definition : definition LEFTBRACKET definition RIGHTBRACKET'

    value1 = p[1]
    value2 = p[3]
    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__


    if False:
        raise SemanticError("Operands given are not of same type")
    if isinstance(value1, str) or isinstance(value1, list):
        if (value2) >= len(value1):
            raise SemanticError()

        p[0] = value1[value2]
    else:
        raise SemanticError()

def p_list_inside_three(p):
    'list_inside : '
    p[0] = []



def p_tuple(p):
    'definition : LEFTPARENTHESIS tupleinside RIGHTPARENTHESIS'
    value2 = p[2]
    p[0] = tuple(value2)

def p_tuple_inside_three(p):
    'tupleinside : '
    p[0] = []

def p_tuple_inside_two(p):
    'tupleinside : definition'
    value1 = p[1]
    p[0] = [value1]


def p_tuple_inside_one(p):
    'tupleinside : definition COMMA tupleinside'
    value1 = p[1]
    value2 = p[3]
    same_type = None
    given_type = value1.__class__.__name__ 
    same_type = value1.__class__.__name__ != value2.__class__.__name__
    p[0] = [value1] + value2


def p_tuple_index_define(p):
    'definition : TUPLE_INDEX definition LEFTPARENTHESIS definition RIGHTPARENTHESIS'
    value1 = p[4]
    value2 = p[2]
    if isinstance(value1, tuple):
        if (value2 - 1) >= len(value1):
            raise SemanticError()

        p[0] = value1[value2 - 1]
    else:
        raise SemanticError()
    
def p_factor_part(p):
    'phase : part'
    value1 = p[1]
    p[0] = value1


def p_phase_get(p):
    'definition : phase'
    value1 = p[1]
    p[0] = value1

def p_part_bool(p):
    'part : BOOLEAN'
    value1 = p[1]
    p[0] = value1

def p_part_number(p):
    'part : NUMBER'
    value1 = p[1]
    p[0] = value1

def p_phase_str(p):
    'phase : STRING'
    value1 = p[1]
    p[0] = value1

def p_error(p):
    raise SyntaxError();


# building the lexer
def main():
    lex.lex()
    input_file = sys.argv[1]
    parsing_code = yacc.yacc()
    sysCode = sys.argv[1]

    try:
        input_file = open(sysCode, "r")
    except Exception as exception:
        print('The exception occured  is ' +type(exception).__name__)
        raise FileNotFoundError
    for read_line in input_file:
        try:
            output = parsing_code.parse(read_line)
        except Exception as exception:
            if (type(exception).__name__ == 'SemanticError'):
                print("SEMANTIC ERROR")
            elif( type(exception).__name__ == 'SyntaxError'):
                print("SYNTAX ERROR")
        else:
            print(output)

if __name__ == "__main__":
    main()