# TesteSparta

## Sistema de Gestão de Companhias Abertas

Este projeto implementa um sistema de gerenciamento de informações sobre companhias abertas, permitindo a persistência e consulta de dados com histórico de alterações.

## Arquivos dentro da pasta

- O arquivo .csv
- Sistema de implantação do banco
- Sistema de exclusão de dados
- Banco de dados
- README
- PDF do Teste

## Requisitos

- Python 3.7+
- SQLite3

## Bibliotecas

- sqlite3
- csv

## Configuração

1. Foi definido a criação, inserção e consulta dos dados

2. Insira dados no banco:

   insert_informacoes('#') ou puxe do .csv

3. Consulte dados:
   print(consulta_informacoes('#'))

## Decisões de Projeto

- **SQLite** foi escolhido pela simplicidade e facilidade de uso para um projeto de pequena escala.
- **Consultas_eficientes**: A estrutura de consulta foi projetada para buscar a informação com data especificada pelo comando {consulta_informacoes()}.
- **Dados_usados**: Com a exigência de consulta por datas dos dados, eu adicionei as datas relativas a coluna de (DT_INI_SIT), pois já esta anexado com a coluna exigida (SIT), e todo o sistema saindo diretamente do arquivo csv.

## BONUS

- Implementei um sistema caso queira excluir alguma tabela do banco.

## AVISO

- Todos os (#) são lugares para você colocar o dado exigido para testar se quiser.

## LINK

<https://github.com/yunkbaza/TesteSparta>

## Agradecimento

A equipe Sparta e Henrique Nakazato,

Gostaria de expressar minha sincera gratidão pela oportunidade de participar do teste para a vaga de desenvolvedor. Agradeço imensamente por considerarem meu perfil e por proporcionarem esse espaço para que eu pudesse demonstrar minhas habilidades e conhecimentos.

É realmente inspirador ver o comprometimento e a dedicação da equipe Sparta em encontrar os melhores talentos para contribuir com seus projetos e objetivos. O profissionalismo e a atenção demonstrados durante todo o processo refletem o valor que vocês atribuem aos candidatos e à construção de uma equipe forte e qualificada.

Henrique, agradeço especialmente por sua orientação e apoio ao longo do teste. Suas insights e feedbacks foram extremamente úteis para o meu desenvolvimento profissional, e estou muito grato pela oportunidade de aprender com alguém tão experiente e dedicado.

Por favor, transmita meus agradecimentos a toda a equipe Sparta. Foi uma experiência enriquecedora e estou ansioso para continuar acompanhando o trabalho de vocês.

Atenciosamente,

Allan Gabriel Baeza