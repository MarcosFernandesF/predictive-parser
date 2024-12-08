
from lexer_analyzer import Lexer

def main():
    analisador_lexico = Lexer()
    tokens = analisador_lexico.analisar("arquivo_teste.txt")

    tabela_de_parsing = {};
    
    if tokens:
        print("Tokens:", tokens)

if __name__ == "__main__":
    main()
