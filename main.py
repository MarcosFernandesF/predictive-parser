from lexer_analyzer import Lexer

def main():
    

    # Definir a tabela de parsing
    tabela_de_parsing = {
        "S": {"$": "MAIN $", "DEF": "MAIN $", "LBRACE": "MAIN $", "INT": "MAIN $", "ID": "MAIN $", "SEMICOLON": "MAIN $", "PRINT": "MAIN $", "RETURN": "MAIN $", "IF": "MAIN $"},
        "MAIN": {"$": "", "DEF": "FLIST", "LBRACE": "STMT", "INT": "STMT", "ID": "STMT", "SEMICOLON": "STMT", "PRINT": "STMT", "RETURN": "STMT", "IF": "STMT"},
        "FLIST": {"DEF": "FDEF FLIST'"},
        "FLIST'": {"$": "", "DEF": "FLIST"},
        "FDEF": {"DEF": "DEF ID_LPAREN PARLIST RPAREN LBRACE STMTLIST RBRACE"},
        "PARLIST": {"RPAREN": "", "INT": "INT ID PARLIST'"},
        "PARLIST'": {"RPAREN": "", "COMMA": "COMMA PARLIST"},
        "VARLIST": {"ID": "ID VARLIST'"},
        "VARLIST'": {"COMMA": "COMMA VARLIST", "SEMICOLON": ""},
        "STMT": {"LBRACE": "LBRACE STMTLIST RBRACE", "INT": "INT VARLIST SEMICOLON", "ID": "ATRIBST SEMICOLON", "SEMICOLON": "SEMICOLON", "PRINT": "PRINTST SEMICOLON", "RETURN": "RETURNST SEMICOLON", "IF": "IFSTMT"},
        "ATRIBST": {"ID": "ID ASSIGN ATRIBST'"},
        "ATRIBST'": {"ID_LPAREN": "FCALL", "ID": "EXPR", "LPAREN": "EXPR", "NUM": "EXPR"},
        "FCALL": {"ID_LPAREN": "ID_LPAREN PARLISTCALL RPAREN"},
        "PARLISTCALL": {"ID": "ID PARLISTCALL'", "RPAREN": ""},
        "PARLISTCALL'": {"RPAREN": "", "COMMA": "COMMA PARLISTCALL"},
        "PRINTST": {"PRINT": "PRINT EXPR"},
        "RETURNST": {"RETURN": "RETURN RETURNST'"},
        "RETURNST'": {"ID": "ID", "SEMICOLON": ""},
        "IFSTMT": {"IF": "IF LPAREN EXPR RPAREN STMT IFSTMT'"},
        "IFSTMT'": {"ELSE": "ELSE STMT"},
        "STMTLIST": {"ID": "STMT STMTLIST'", "LBRACE": "STMT STMTLIST'", "INT": "STMT STMTLIST'", "SEMICOLON": "STMT STMTLIST'", "PRINT": "STMT STMTLIST'", "RETURN": "STMT STMTLIST'", "IF": "STMT STMTLIST'"},
        "STMTLIST'": {"ID": "STMTLIST", "LBRACE": "STMTLIST", "RBRACE": "", "INT": "STMTLIST", "SEMICOLON": "STMTLIST", "PRINT": "STMTLIST", "RETURN": "STMTLIST", "IF": "STMTLIST"},
        "EXPR": {"ID": "NUMEXPR EXPR'", "LPAREN": "NUMEXPR EXPR'", "NUM": "NUMEXPR EXPR'"},
        "EXPR'": {"RPAREN": "", "SEMICOLON": "", "LT": "LT NUMEXPR", "LE": "LE NUMEXPR", "GT": "GT NUMEXPR", "GE": "GE NUMEXPR", "EQ": "EQ NUMEXPR", "NE": "NE NUMEXPR"},
        "NUMEXPR": {"ID": "TERM NUMEXPR'", "LPAREN": "TERM NUMEXPR'", "NUM": "TERM NUMEXPR'"},
        "NUMEXPR'": {"RPAREN": "", "SEMICOLON": "", "LT": "", "LE": "", "GT": "", "GE": "", "EQ": "", "NE": "", "PLUS": "PLUS TERM NUMEXPR'", "MINUS": "MINUS TERM NUMEXPR'"},
        "TERM": {"ID": "FACTOR TERM'", "LPAREN": "FACTOR TERM'", "NUM": "FACTOR TERM'"},
        "TERM'": {"RPAREN": "", "SEMICOLON": "", "LT": "", "LE": "", "GT": "", "GE": "", "EQ": "", "NE": "", "PLUS": "", "MINUS": "", "TIMES": "TIMES FACTOR TERM'", "DIVIDE": "DIVIDE FACTOR TERM'"},
        "FACTOR": {"ID": "ID", "LPAREN": "LPAREN NUMEXPR RPAREN", "NUM": "NUM"}
    }

    analisador_lexico = Lexer()
    tokens = analisador_lexico.obter_tokens("arquivo_teste.txt")
    print(tokens);

if __name__ == "__main__":
    main()
