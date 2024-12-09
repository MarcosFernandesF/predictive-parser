# README - Parte 3: Parser preditivo para a linguagem dada.

**Autor:** Marcos Roberto Fernandes Filho  
**Matrícula:** 22100915

## Versões e Depedências Utilizadas

- Python 3.12.3
- pip (gerenciador de pacotes do Python)
- biblioteca PLY.

## Instruções de Instalação

### 1. Instalar Python e pip

Se você não tem o Python instalado, siga os passos abaixo:

1. Abra o terminal.
2. Atualize o gerenciador de pacotes:

   ```bash
   sudo apt update
   ```

3. Instale o Python:

    ```bash
   sudo apt install python3
   ```
4. Instale o pip:

    ```bash
   sudo apt install python3-pip
   ```

### 2. Criar um Ambiente Virtual

Necessário para rodar o PLY.

1. Instale o ```venv```

2. Navegue até o diretório onde o projeto está localizado:

   ```bash
   cd /caminho/para/o/projeto
   ```

3. Crie o ambiente virtual:

   ```bash
   python3 -m venv nome-do-ambiente
   ```

4. Ative o ambiente virtual:

   ```bash
   source /nome-do-ambiente/bin/activate
   ```

### 3. Instalando o PLY

Com o ambiente virtual ativado, simplesmente instale a biblioteca PLY:

   ```bash
   pip install ply
   ```
  
## Execução do Projeto

### Como Executar o Parser Preditivo

Para rodar o projeto, siga os passos abaixo:

1. Navegue até o diretório onde o código do parser está localizado. Se você estiver usando um ambiente virtual, certifique-se de que o mesmo esteja ativado (como mencionado na seção de instalação).

2. Execute o parser com o arquivo de entrada desejado. O comando básico para execução é:

   ```bash
   python3 main.py <caminho-do-arquivo>
   ```

3. "caminho-do-arquivo" é o caminho para o arquivo de código fonte que você deseja analisar. Exemplo:

   ```bash
   python3 main.py arquivo_certo.txt
   ```

### Observação: Modo Debug

O projeto inclui uma funcionalidade de modo debug que permite acompanhar o processo de parsing com mais detalhes. Quando o modo de debug está ativado, o sistema imprime informações sobre a pilha, os tokens processados e as produções aplicadas durante a execução do parser.

#### Como ativar o modo debug.

Por padrão, o modo de debug está desativado. Para ativá-lo, basta alterar o valor da variável modo_debug para True no código do parser. No arquivo parser.py, localize a seguinte linha:

   ```python
   modo_debug = False
   ```

E altere para:

   ```python
   modo_debug = True
   ```