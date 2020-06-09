# Mukesh Goud Kondeti
# 112689870

import sys
import warnings
import ply.lex as lex
import ply.yacc as yacc

warnings.simplefilter("ignore", category = FutureWarning)

#Exception Classes
class SyntaxError(Exception):
    pass
class SemanticError(Exception):
    pass

# Propositional Logic Grammar

# AST Nodes : class definitions
class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0

    def __str__(self):
        return 0

    def __eq__(self, node):
        return 0

class NodeBlock(Node):
    def __init__(self, list_statements):
        self.list_statements = list_statements

    def execute(self):
        if len(self.list_statements) > 0:
            i = 0
            while i < len(self.list_statements):
                self.list_statements[i].execute()
                i += 1

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeNumber(Node):
    def __init__(self, value):
        if ('e' in value):
            self.value = float(value)
        if('.' in value):
            self.value = float(value)
        else:
            self.value = int(value)

    def evaluate(self):
        return self.value

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeTuple(Node):
    def __init__(self, value1, value2):
        self.value = [value1, value2]
    def evaluate(self):
        return_list = []
        i = 0
        while i < len(self.value):
            element = self.value[i]
            if(type(element) == list):
                return_list.append(element)
            elif(type(element) != list):
                return_list.append(element.evaluate())
            i += 1    
        return tuple(return_list)

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeList(Node):
    def __init__(self, value):
        self.value = [value]
    def evaluate(self):
        return_list = []
        i = 0
        while i < len(self.value):
            element = self.value[i]
            if(type(element) == list):
                return_list.append(element)
            elif(type(element) != list):
                return_list.append(element.evaluate())
            i += 1      
        return return_list

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeString(Node):
    def __init__(self, value):
        self.value = str(value)[1:-1]

    def evaluate(self):
        return self.value

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeBoolean(Node):
    def __init__(self, value):
        if value !='True':
            self.value = False
        elif value =='True':
            self.value = True

    def evaluate(self):
        return self.value

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

# program statements
class NodeOfPrint(Node):
    def __init__(self, to_print):
        self.to_print = to_print

    def execute(self):
        print(self.to_print.evaluate())

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeOfAssignment(Node):
    def __init__(self, name, expression):
        self.expression = expression
        self.name = name 

    def execute(self):
        names[self.name.value] = self.expression.evaluate()

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeOfAssignmentList(Node):
    def __init__(self, node, element):
        self.index_element = node.index_element
        self.group_of_elements = node.group_of_elements
        self.element = element

    def execute(self):
        index_element = self.index_element.evaluate()
        group_of_elements = self.group_of_elements.evaluate()
        if (type(group_of_elements) == tuple or type(group_of_elements) == str):
            raise SemanticError()
        else:
            group_of_elements[index_element] = self.element.evaluate()

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeOfIFBlock(Node):
    def __init__(self, condition, blockOfCode):
        self.block = blockOfCode
        self.condition = condition

    def execute(self):
        if(self.condition.evaluate()):
            self.block.execute()

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeOfElseBlock(Node):
    def __init__(self, ifstatement, elseblock):
        self.condition = ifstatement.condition
        self.ifb = ifstatement.block
        self.elseb = elseblock

    def execute(self):
        if(not self.condition.evaluate()):
            self.elseb.execute()
        else:
            self.ifb.execute()

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeOfWhileBlock(Node):
    def __init__(self, expression, block):
        self.expression = expression
        self.block = block

    def execute(self):
        while(self.expression.evaluate()):
            self.block.execute()

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

# Binary Operations
class NodeSummation(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    
    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if (((type(self.value1.evaluate()) == list) and (type(self.value2.evaluate()) == list)) or ((type(self.value1.evaluate()) ==  int or  type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int or type(self.value2.evaluate()) == float))):
            return self.value1.evaluate() + self.value2.evaluate()
        elif ((type(self.value1.evaluate()) == tuple) and (type(self.value2.evaluate()) == tuple)):
            return self.value1.evaluate() + self.value2.evaluate()
        elif (((type(self.value1.evaluate()) ==  str) and (type(self.value2.evaluate()) == str))):
            return self.value1.evaluate() + self.value2.evaluate() 
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeDifference(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        
    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if ((type(self.value1.evaluate()) ==  int or type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int or type(self.value2.evaluate()) == float)):
            return self.value1.evaluate() - self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeProduct(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    
    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if ((type(self.value1.evaluate()) ==  int or  type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int or type(self.value2.evaluate()) == float)):
            return self.value1.evaluate() * self.value2.evaluate()
        else:
            raise SemanticError()
    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeDivide(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if (((type(self.value1.evaluate()) ==  int or type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int) or type(self.value2.evaluate()) == float) and self.value2.evaluate() != 0):
            return self.value1.evaluate() / self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeFloorDivide(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if (((type(self.value1.evaluate()) ==  int or type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int) or type(self.value2.evaluate()) == float) and self.value2.evaluate() != 0):
            return self.value1.evaluate() // self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeModulus(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if (((type(self.value1.evaluate()) ==  int or type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int) or type(self.value2.evaluate()) == float) and self.value2.evaluate() != 0):
            return self.value1.evaluate() % self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodePower(Node):
    def __init__(self, value1, value2, operator):
        self.value1 = value1
        self.value2 = value2
        self.operator = operator
        

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if ((type(self.value1.evaluate()) ==  int or type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int or type(self.value2.evaluate()) == float)):
            return self.value1.evaluate() ** self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeMembership(Node):
    def __init__(self, value1, value2, operator):
        self.value1 = value1
        self.value2 = value2
        self.operator = operator

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if((type(self.value1.evaluate()) ==  str) and (type(self.value2.evaluate()) == str)):
            return self.value1.evaluate() in self.value2.evaluate()
        elif(type(self.value2.evaluate()) == list or type(self.value2.evaluate()) ==  tuple):
            return self.value1.evaluate() in self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeConcat(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if(type(self.value2.evaluate()) == list):
            result = self.value2.evaluate()
            if(type(self.value1.evaluate()) == list):
                result = NodeList(self.value1.evaluate()).evaluate() + result
                return result
            else:
                result.insert(0, self.value1.evaluate())
                return result
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeLesserThan(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if((type(self.value1.evaluate()) ==  int or type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int or type(self.value2.evaluate()) == float)):
            return self.value1.evaluate() < self.value2.evaluate()
        elif ((type(self.value1.evaluate()) ==  str) and (type(self.value2.evaluate()) == str)):
            return self.value1.evaluate() < self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeLesserThanEqual(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if((type(self.value1.evaluate()) ==  int or type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int or type(self.value2.evaluate()) == float)):
            return self.value1.evaluate() <= self.value2.evaluate()
        elif ((type(self.value1.evaluate()) ==  str) and (type(self.value2.evaluate()) == str)):
            return self.value1.evaluate() <= self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeGreaterThan(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__
        
        if((type(self.value1.evaluate()) ==  int or type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int or type(self.value2.evaluate()) == float)):
            return self.value1.evaluate() > self.value2.evaluate()
        elif ((type(self.value1.evaluate()) ==  str) and (type(self.value2.evaluate()) == str)):
            return self.value1.evaluate() > self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeGreaterThanEqual(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__
        
        if((type(self.value1.evaluate()) ==  int or type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int or type(self.value2.evaluate()) == float)):
            return self.value1.evaluate() >= self.value2.evaluate()
        elif ((type(self.value1.evaluate()) ==  str) and (type(self.value2.evaluate()) == str)):
            return self.value1.evaluate() >= self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeEqual(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__
        
        if((type(self.value1.evaluate()) ==  int or type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int or type(self.value2.evaluate()) == float)):
            return self.value1.evaluate() == self.value2.evaluate()
        elif ((type(self.value1.evaluate()) ==  str) and (type(self.value2.evaluate()) == str)):
            return self.value1.evaluate() == self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeNotEqual(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__
        
        if((type(self.value1.evaluate()) ==  int or type(self.value1.evaluate()) == float) and (type(self.value2.evaluate()) == int or type(self.value2.evaluate()) == float)):
            return self.value1.evaluate() != self.value2.evaluate()
        elif ((type(self.value1.evaluate()) ==  str) and (type(self.value2.evaluate()) == str)):
            return self.value1.evaluate() != self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeLogicalOR(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if((isinstance(self.value1.evaluate(), bool)) and (isinstance(self.value2.evaluate(), bool))):
            return self.value1.evaluate() or self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeLogicalAND(Node):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value2.__class__.__name__

        if((isinstance(self.value1.evaluate(), bool)) and (isinstance(self.value2.evaluate(), bool))):
            return self.value1.evaluate() and self.value2.evaluate()
        else:
            raise SemanticError()

    def __str__(self):
        return self.evaluate()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeName(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        try:
            return names[self.value]
        except:
            raise SemanticError()

    def __str__(self):
        return self.execute()

class NodeUnary(Node):
    def __init__(self, operator, value1):
        self.value1 = value1
        self.operator = operator
        self.list1 = ['-', 'not', '+']

    def evaluate(self):
        given_type = self.value1.__class__.__name__ 
        same_type = self.value1.__class__.__name__ != self.value1.__class__.__name__

        if(self.operator == self.list1[2]):
            if(type(self.value1.evaluate()) == int or (type(self.value1.evaluate()) == float)):
                return self.value1.evaluate()
            else:
                raise SemanticError()
        elif(self.operator == self.list1[0]):
            if((type(self.value1.evaluate()) == int) or (type(self.value1.evaluate()) == float)):
                return -self.value1.evaluate()
            else:
                raise SemanticError()
        elif(self.operator.value == self.list1[1]):
            if(type(self.value1.evaluate()) == bool):
                return not self.value1.evaluate()
            else:
                raise SemanticError()    

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeOfIndex(Node):
    def __init__(self, group_of_elements, index_element):
        self.group_of_elements = group_of_elements
        self.index_element = index_element

    def evaluate(self):
        if((type(self.group_of_elements.evaluate()) == str) or (type(self.group_of_elements.evaluate()) == list)):
            if(type(self.index_element.evaluate()) == int):
                try:
                    return self.group_of_elements.evaluate()[self.index_element.evaluate()]
                except Exception:
                    raise SemanticError()
        raise SemanticError()

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

class NodeOfPound(Node):
    def __init__(self, group_of_elements, index_element):
        self.group_of_elements = group_of_elements
        self.index_element = index_element

    def evaluate(self):
        if(type(self.group_of_elements.evaluate()) == tuple):
            if(type(self.index_element.evaluate()) == int):
                try:
                    return self.group_of_elements.evaluate()[self.index_element.evaluate()-1]
                except Exception:
                    raise SemanticError()
        raise SemanticError()

    def __str__(self):
        return self.execute()

    def __eq__(self, node):
        if (type(self.execute()) == type(node.execute())):
            return True
        else:
            return False

# dictionary of names
names = {}
#reserved keywords
reserved = {
    'in' : 'IN',
    'print' : 'PRINTSTATEMENT',
    'orelse' : 'ORELSE',
    'not' : 'NEGATION',
    'andalso' : 'ANDALSO',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'if' : 'IF' ,
    'div':'INTDIV' 
 }

#program tokens
tokens = [
    'NAME',
    'LESSERTHAN', 
    'LESSEREQUAL', 
    'EQUAL', 
    'NOTEQUAL', 
    'GREATERTHAN', 
    'GREATEREQUAL',
    'ASSIGNMENT',
    'CONCAT',
    'SUMMATION',
    'DIFFERENCE', 
    'PRODUCT',
    'DIVIDE',
    'POWER',
    'LEFTSQAUREBRACKET', 
    'RIGHTSQAUREBRACKET',
    'LEFTPARANTHESIS', 
    'RIGHTPARANTHESIS', 
    'LEFTCURLYBRACKET', 
    'RIGHTCURLYBRACKET',
    'TUPLEPOUND',
    'COMMA', 
    'SEMICOLON',
    'NUMBER',
    'TRUE', 
    'FALSE',
    'STRING',
    'PRINTSTATEMENT',
    'IF',
    'ELSE',
    'WHILE',
    'ORELSE',
    'ANDALSO',
    'IN',
    'MODULUS',
    'INTDIV',
    'NEGATION',
    ]

#parser identification symbols
t_ASSIGNMENT = r'='
t_LESSERTHAN = r'<'
t_LESSEREQUAL = r'<='
t_PRODUCT   = r'\*'
t_RIGHTCURLYBRACKET = r'\}'
t_LEFTCURLYBRACKET = r'\{'
t_EQUAL = r'=='
t_NOTEQUAL = r'<>'
t_TUPLEPOUND = r'\#'
t_GREATERTHAN = r'>'
t_RIGHTPARANTHESIS  = r'\)'
t_LEFTPARANTHESIS  = r'\('
t_SEMICOLON    = r';'
t_COMMA   = r','
t_GREATEREQUAL = r'>='
t_RIGHTSQAUREBRACKET = r'\]'
t_LEFTSQAUREBRACKET = r'\['
t_CONCAT = r'::'
t_POWER = r'\*\*'
t_DIVIDE  = r'/'
t_DIFFERENCE  = r'-'
t_SUMMATION    = r'\+'

# Ignored characters
t_ignore = " \t"

# methods for parser identification symbols 
def t_NUMBER(t):
    r'\d*(\d\.|\.\d)\d*([eE]-?\d+)?|\d+'
    try:
        t.value = NodeNumber(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_TRUE(t):
    r'True'
    t.value = NodeBoolean(t.value)
    return t    

def t_STRING(t):
    r'(\'(\\\n|\\\\|\\\"|\\\'|\\\t|[^\\\'])*\')|(\"(\\\n|\\\\|\\\"|\\\'|\\\t|[^\\\"])*\")'
    t.value = NodeString(t.value)
    return t

def t_FALSE(t):
    r'False'
    t.value = NodeBoolean(t.value)
    return t

def t_INTDIV(t):
    r'div'
    t.type = reserved.get(t.value,'INTDIV')
    return t

def tokenize(inp):
    lexer.input(inp)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

def t_MOD(t):
    r'mod'
    t.type = reserved.get(t.value,'MODULUS')
    return t

def t_NAME(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')
    t.value = NodeName(t.value)
    return t

#error tokens
def t_error(t):
    raise SyntaxError()

# Parsing precedence rules
precedence = (
    ('right', 'ASSIGNMENT'),
    ('left', 'PRINTSTATEMENT'),
    ('left', 'ORELSE'),
    ('left', 'ANDALSO'),
    ('left', 'NEGATION'),
    ('left', 'GREATERTHAN', 'LESSEREQUAL', 'LESSERTHAN', 'GREATEREQUAL', 'EQUAL', 'NOTEQUAL'),
    ('right', 'CONCAT'),
    ('left', 'IN'),
    ('left','SUMMATION', 'DIFFERENCE'),
    ('left','PRODUCT', 'DIVIDE', 'INTDIV', 'MODULUS'),
    ('right', 'POWER'),
    ('left', 'LEFTSQAUREBRACKET', 'RIGHTSQAUREBRACKET'),
    ('left', 'TUPLEPOUND'),
    ('left', 'LEFTPARANTHESIS', 'RIGHTPARANTHESIS')
    )

#parser production definitions
def p_single_program(p):
    'instruction : program'
    value1 = p[1]
    p[0] = value1

def p_assign_instruction_list(p):
    'instruction : list_instruction_assignment'
    value1 = p[1]
    p[0] = value1

def p_list_instruction(p):
    'list_instruction : list_instruction instruction'
    value1 = p[1]
    value2 = p[2]
    p[0] = value1 + [value2]

def p_program(p):
    'program : LEFTCURLYBRACKET list_instruction RIGHTCURLYBRACKET'
    value2 = p[2]
    p[0] = NodeBlock(value2)

def p_print_instruction(p):
    'instruction : instruction_print'
    value1 = p[1]
    p[0] = value1

def p_assign_instruction(p):
    'instruction : instruction_assignment'
    value1 = p[1]
    p[0] = value1

def p_empty_program(p):
    'program : LEFTCURLYBRACKET RIGHTCURLYBRACKET'
    value_empty = []
    p[0] = NodeBlock(value_empty)

def p_list_instruction_val(p):
    'list_instruction : instruction'
    value1 = p[1]
    p[0] = [value1]

def p_conditional_if_instruction(p):
    'instruction : if_instruction'
    value1 = p[1]
    p[0] = value1

def p_if_instruction(p):
    'if_instruction : IF LEFTPARANTHESIS definition RIGHTPARANTHESIS program'
    value1 = p[3]
    value2 = p[5]
    p[0] = NodeOfIFBlock(value1, value2)

def p_conditional_while_instruction(p):
    'instruction : while_instruction'
    value1 = p[1]
    p[0] = value1

def p_while_instruction(p):
    'while_instruction : WHILE LEFTPARANTHESIS definition RIGHTPARANTHESIS program'
    value1 = p[3]
    value2 = p[5]
    p[0] = NodeOfWhileBlock(value1, value2)

def p_conditional_else_instruction(p):
    'instruction : else_instruction'
    value1 = p[1]
    p[0] = value1

def p_else_instruction(p):
    'else_instruction : if_instruction ELSE program'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeOfElseBlock(value1, value2)

def p_instruction_assignment(p):
    'instruction_assignment : NAME ASSIGNMENT definition SEMICOLON'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeOfAssignment(value1, value2)

def p_assign_list_smt(p):
    'list_instruction_assignment : index ASSIGNMENT definition SEMICOLON'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeOfAssignmentList(value1, value2)

def p_instruction_print(p):
    'instruction_print : PRINTSTATEMENT LEFTPARANTHESIS definition RIGHTPARANTHESIS SEMICOLON'
    value1 = p[3]
    p[0] = NodeOfPrint(value1)
    
def p_list(p):
    'list : LEFTSQAUREBRACKET inner_list RIGHTSQAUREBRACKET'
    value1 = p[2]
    p[0] = value1

def p_leaf_list_definition(p):
    'definition : list'
    value1 = p[1]
    p[0] = value1

def p_tuple(p):
    'tuple : LEFTPARANTHESIS inner_tuple RIGHTPARANTHESIS'
    value1 = p[2]
    p[0] = value1

def p_inner_list(p):
    'inner_list : inner_list COMMA definition'
    value3 = p[3]
    value1 = p[1]
    value1.value.append(value3)
    p[0] = value1

def p_inner_tuple(p):
    'inner_tuple : definition COMMA definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeTuple(value1, value2)

def p_inner_list_two(p):
    'inner_list : definition'
    value1 = p[1]
    p[0] = NodeList(value1)

def p_inner_tuple_two(p):
    'inner_tuple : inner_tuple COMMA definition'
    value3 = p[3]
    value1 = p[1]
    value1.value.append(value3)
    p[0] = value1

def p_product_definition(p):
    'definition : definition PRODUCT definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeProduct(value1, value2)

def p_difference_definition(p):
    'definition : definition DIFFERENCE definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeDifference( value1, value2 )

def p_summation_definition(p):
    'definition : definition SUMMATION definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeSummation(value1, value2)

def p_floor_division_definition(p):
    'definition : definition INTDIV definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeFloorDivide( value1, value2)

def p_divide_definition(p):
    'definition : definition DIVIDE definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeDivide(value1, value2)

def p_power_definition(p):
    'definition : definition POWER definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodePower(value1, value2, p[2])

def p_modulus_definition(p):
    'definition : definition MODULUS definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeModulus( value1, value2)

def p_concat_definition(p):
    'definition : definition CONCAT definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeConcat(value1, value2)

def p_membership_definition(p):
    'definition : definition IN definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeMembership(value1, value2, p[2])

def p_leaf_tuple_definition(p):
    'definition : tuple'
    value1 = p[1]
    p[0] = value1

def p_relational_lessthan_definition(p):
    'definition : definition LESSERTHAN definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeLesserThan(value1, value2)

def p_relational_greaterthan_definition(p):
    'definition : definition GREATERTHAN definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeGreaterThan(value1, value2)

def p_relational_lessthan_or_equal_definition(p):
    'definition : definition LESSEREQUAL definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeLesserThanEqual(value1, value2)

def p_relational_greaterthan_or_equal_definition(p):
    'definition : definition GREATEREQUAL definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeGreaterThanEqual(value1, value2)

def p_leaf_string_definition(p):
    'definition : STRING'
    value1 = p[1]
    p[0] = value1

def p_relational_not_equal_definition(p):
    'definition : definition NOTEQUAL definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeNotEqual(value1, value2)

def p_relational_equal_definition(p):
    'definition : definition EQUAL definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeEqual(value1, value2)

def p_logical_and_definition(p):
    'definition : definition ANDALSO definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeLogicalAND(value1, value2)

def p_definition_pound(p):
    'pound : TUPLEPOUND definition definition '
    value1 = p[3]
    value2 = p[2]
    p[0] = NodeOfPound(value1, value2)

def p_leaf_number_definition(p):
    'definition : NUMBER'
    value1 = p[1]
    p[0] = value1

def p_logical_or_definition(p):
    'definition : definition ORELSE definition'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeLogicalOR( value1, value2)

def p_unary_minus_definition(p):
    'definition : DIFFERENCE definition'
    value1 = p[1]
    value2 = p[2]
    p[0] = NodeUnary(value1, value2)

def p_definition_index(p):
    'index : definition LEFTSQAUREBRACKET definition RIGHTSQAUREBRACKET'
    value1 = p[1]
    value2 = p[3]
    p[0] = NodeOfIndex(value1, value2)
    
def p_unary_plus_expression(p):
    'definition : SUMMATION definition'
    value1 = p[1]
    value2 = p[2]
    p[0] = NodeUnary(value1, value2)

def p_definition_group(p):
    'definition : LEFTPARANTHESIS definition RIGHTPARANTHESIS'
    p[0] = p[2]

def p_leaf_true_definition(p):
    'definition : TRUE'
    value1 = p[1]
    p[0] = value1

def p_factor_part(p):
    'phase : part'
    value1 = p[1]
    p[0] = value1

def p_phase_get(p):
    'definition : phase'
    value1 = p[1]
    p[0] = value1

def p_part_bool(p):
    'part : '
    p[0] = None

def p_leaf_false_definition(p):
    'definition : FALSE'
    value1 = p[1]
    p[0] = value1

def p_leaf_index_definition(p):
    'definition : index'
    value1 = p[1]
    p[0] = value1

def p_unary_not_definition(p):
    'definition : NEGATION definition'
    value1 = p[1]
    value2 = p[2]
    p[0] = NodeUnary(value1, value2)

def p_leaf_pound_definition(p):
    'definition : pound'
    value1 = p[1]
    p[0] = value1

def p_leaf_name_definition(p):
    'definition : NAME'
    value1 = p[1]
    p[0] = value1

def p_error(p):
    raise SyntaxError()

def main():
    lex.lex()
    yacc.yacc()
    if (len(sys.argv) == 2):
        try:
            read_contents = sys.argv[1]
            with open(read_contents, 'r') as inputfile:
                read_data = inputfile.read().replace('\n', '')
            root = yacc.parse(read_data)
            root.execute()
        except Exception as exception:
            if (type(exception).__name__ == 'SemanticError'):
                print("SEMANTIC ERROR")
            elif( type(exception).__name__ == 'SyntaxError'):
                print("SYNTAX ERROR")
            else:
                print("SYNTAX ERROR")
    else:
        print("invalid number of arguments... Please run program correctly")

if __name__ == "__main__":
    main()