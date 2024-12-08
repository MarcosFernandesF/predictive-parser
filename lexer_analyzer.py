import ply.lex as lex

# Lista de tokens
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
    'def': 'DEF',
    'print': 'PRINT',
    'return': 'RETURN'
}

# Adicionando palavras reservadas aos tokens
tokens += list(reservadas.values())

# Expressões regulares simples
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

# Função para identificadores que terminam com parênteses
def t_ID_LPAREN(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*\('
    t.type = 'ID_LPAREN'
    return t

# Função para identificar IDs e palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    return t

# Função para números
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)  # Converte para inteiro
    return t

# Caracteres ignorados
t_ignore = ' \t\n'

# Função para tratar erros
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
