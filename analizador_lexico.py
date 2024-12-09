#####################################################
# Parte 3 - Parser Preditivo para linguagem dada.   #
# Autor - Marcos Roberto Fernandes Filho (22100915) #
#####################################################

import ply.lex as lex

# Lista de tokens disponíveis
tokens = [
    'ID', 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',
    'ASSIGN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COMMA', 'SEMICOLON',
    'ID_LPAREN'
]

# Palavras reservadas
reservadas = {
    'int': 'INT',
    'if': 'IF',
    'else': 'ELSE',
    'endif': 'ENDIF',
    'def': 'DEF',
    'print': 'PRINT',
    'return': 'RETURN'
}

# Adicionando palavras reservadas aos tokens
tokens += list(reservadas.values())

# Expressões regulares simples para operadores e símbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_ASSIGN = r':='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'

# Reconhece identificadores terminados com '('
def t_ID_LPAREN(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*\('
    t.type = 'ID_LPAREN'
    return t

# Reconhece identificadores e palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    return t

# Reconhece números
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)  # Converte para inteiro
    return t

# Ignora espaços e tabulações
t_ignore = ' \t\n'

# Lida com caracteres inválidos
def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

# Constrói o lexer
lexer = lex.lex()

# Classe para encapsular o lexer
class Lexer:
    def __init__(self):
        self.lexer = lexer

    def obter_tokens(self, file_path):
        tipos = []
        try:
            with open(file_path, 'r') as file:
                data = file.read()
                self.lexer.input(data)
                for token in self.lexer:
                    tipos.append(token.type)
                tipos.append("$")
                return tipos
        except FileNotFoundError:
            print(f"Arquivo {file_path} não foi encontrado.")
