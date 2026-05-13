# Leitor de CSV para SQLite

Este é um projeto simples em Python desenvolvido para ler dados de empresas de capital aberto a partir de um arquivo CSV (geralmente extraído da CVM) e armazenar as informações mais relevantes em um banco de dados SQLite para consultas rápidas.

## 📁 Estrutura dos Arquivos

* **`teste.py`**: É o script principal do projeto. Ele é responsável por:
    * Ler o arquivo `cad_cia_aberta.csv`.
    * Criar o banco de dados local `informacoes.db` com a tabela `informacoes` (caso não exista).
    * Filtrar as colunas de interesse (CNPJ, Denominação Social, Situação e Data de Início da Situação) e inseri-las no banco.
    * Executar uma consulta de teste no final da execução.
* **`excluir_informacao.py`**: Script auxiliar criado para remover registros específicos do banco de dados. 
    * *Nota para desenvolvimento: O script atualmente tenta deletar de uma tabela chamada `pessoas`. Para funcionar com o script principal, será necessário alterar o nome da tabela no código para `informacoes` e a coluna para `DT_INI_SIT`.*
* **`cad_cia_aberta.csv`**: Arquivo de origem contendo os dados separados por ponto e vírgula (`;`). Deve ser colocado na mesma pasta dos scripts.

## 🚀 Tecnologias e Dependências

O projeto utiliza apenas bibliotecas nativas do Python, portanto, não é necessário instalar pacotes externos via `pip`.
* **Python 3.x**
* `sqlite3` (Manipulação do banco de dados)
* `csv` (Leitura do arquivo de dados)

## ⚙️ Como executar

1. Clone este repositório ou baixe os arquivos.
2. Certifique-se de que o arquivo de dados `cad_cia_aberta.csv` esteja na mesma pasta que os scripts Python.
3. Abra o terminal na pasta do projeto e execute o script de importação:

   python teste.py


4. Após a execução, o arquivo `informacoes.db` será criado automaticamente na pasta e o terminal exibirá o resultado da consulta de teste.
5. Para testar a exclusão de dados, ajuste a query SQL no arquivo de exclusão e execute:

python excluir_informacao.py


## 🛠️ Personalização

* **Filtros de Consulta:** No final do arquivo `teste.py`, a função `consulta_informacoes('#')` está configurada para buscar a string `#`. Altere esse parâmetro para uma data válida no formato presente no seu CSV (ex: `'2023-01-01'`) para retornar resultados reais.
