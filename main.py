#####################################################
# Parte 3 - Parser Preditivo para linguagem dada.   #
# Autor - Marcos Roberto Fernandes Filho (22100915) #
#####################################################

import sys
import os
from analizador_lexico import Lexer

def parse(tokens_de_entrada, tabela_de_parsing, terminais):

    modo_debug = False; # Define se informações de debug serão exibidas.

    if modo_debug:
        print("Iniciando o parser com os tokens de entrada:", tokens_de_entrada)

    # Inicializa a pilha com o símbolo inicial e o marcador final
    pilha = ["MAIN", "$"]
    indice_simbolo_atual = 0
    topo_pilha = pilha[indice_simbolo_atual]
    sucesso = True

    # Armazena matchs realizados para exibição posterior
    matchs_realizados = []

    # Enquanto o topo da pilha for diferente de $.
    while topo_pilha != "$":

        simbolo_atual = tokens_de_entrada[indice_simbolo_atual]
        
        if modo_debug:
            print(f"\nPilha: {pilha} | Símbolo atual: {simbolo_atual}")

         # Caso terminal na pilha seja igual ao token atual = MATCH.
        if topo_pilha == simbolo_atual:
            matchs_realizados.append(f"{topo_pilha} == {simbolo_atual}")
            pilha.pop(0)
            indice_simbolo_atual += 1

            if modo_debug:
                print(f"MATCH {topo_pilha} com {simbolo_atual}")

        # Caso de erro: símbolo na pilha é terminal, mas não casa com o token atual.
        elif topo_pilha in terminais:
            print(f"ERRO: Símbolo terminal não está na lista de terminais: {topo_pilha}")
            sucesso = False
            break

        # Caso de erro: produção não encontrada na tabela.
        elif topo_pilha not in tabela_de_parsing or simbolo_atual not in tabela_de_parsing[topo_pilha]:
            print(f"ERRO: Não existe produção para: {topo_pilha} com {simbolo_atual}")
            sucesso = False
            break

        # Produção encontrada na tabela
        else:
            producao = tabela_de_parsing[topo_pilha][simbolo_atual]

            if modo_debug:
                print(f"Produção encontrada: {producao}")

            pilha.pop(0)

            if producao != "":
                producao = producao.split(" ")
                producao.reverse()
                for simbolo in producao:
                    pilha.insert(0, simbolo)

                if modo_debug:
                    print(f"Nova pilha após a produção: {pilha}")
            else:
                if modo_debug:
                    print("Produção epsilon (sem símbolos a adicionar à pilha)")

        topo_pilha = pilha[0]

    if sucesso:
        print("\nParsing concluído com sucesso!")
        print("\nSequências de matches:");
        for indice, match in enumerate(matchs_realizados, start=1):  # start=1 para começar a contagem do índice a partir de 1
            print(f"{indice}. {match}")
        print("\nNumero de matches: ", len(matchs_realizados))
            
    else:
        print("\nParsing falhou.")

def main():
    if len(sys.argv) != 2:
        print("Uso correto: python main.py <nome_do_arquivo>")
        return

    nome_arquivo = sys.argv[1]

    if not os.path.isfile(nome_arquivo):
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return

    terminais_da_tabela = (
        'ID', 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LT', 'GT', 'LE', 'GE', 'NE', 'EQ',
        'ASSIGN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COMMA', 'SEMICOLON', 'INT', 'IF',
        'ELSE', 'DEF', 'PRINT', 'RETURN', 'ID_LPAREN'
    )

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
        "IFSTMT'": {"ELSE": "ELSE STMT ENDIF", "ENDIF": "ENDIF"},
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
    tokens = analisador_lexico.obter_tokens(nome_arquivo)

    parse(tokens, tabela_de_parsing, terminais_da_tabela)

if __name__ == "__main__":
    main()
