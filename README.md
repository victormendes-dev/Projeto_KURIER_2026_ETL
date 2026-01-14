ETL API Local – Projeto de Demonstração
Visão Geral:

Este projeto consiste em um ETL (Extract, Transform, Load) desenvolvido em Python, responsável por recuperar, tratar e carregar dados provenientes de uma API Local, criada para fins avaliativos em um desafio técnico para a vaga de Desenvolvedor Pleno.

O pipeline realiza a extração de três arquivos JSON, aplica transformações e padronizações necessárias e insere os dados em um banco de dados relacional PostgreSQL, deixando-os prontos para consumo por ferramentas de BI, como o Power BI.

Projeto Relacionado:
A API utilizada neste ETL está disponível no repositório abaixo:
	👉 https://github.com/victormendes-dev/Projeto_KURIER_2026_API
Para que o ETL funcione corretamente, é necessário iniciar a API localmente por meio do arquivo .bat, mantendo-a ativa durante a execução do processo.

Estrutura da Solução:
A solução foi organizada em módulos bem definidos, seguindo o fluxo natural de um processo de ETL, separando responsabilidades e facilitando manutenção, entendimento e evolução do projeto.

src/
  Diretório principal do projeto, onde está concentrada toda a lógica do ETL.

inicializacao/
- Responsável pelo início do processo de ETL.
- Contém os scripts que realizam:
- Requisições à API Local
- Recuperação dos arquivos JSON (leads, clientes, vendas)
- Representa a etapa Extract do ETL.

models/
- Camada responsável pela padronização e modelagem dos dados.
- Define a estrutura das entidades do projeto por meio de classes.
- Garante consistência de tipos, ordem dos campos e organização dos dados antes da carga.
- Exemplo: modelagem da entidade LEADS, encapsulando atributos e método de conversão (to_tuple) para facilitar a inserção no banco.
- Essa camada representa a base da etapa Transform, assegurando que os dados sigam um padrão único em todo o pipeline.

guardar_dados/
- Responsável por persistir os dados transformados.
- Converte os arquivos JSON em CSV
- Cria uma camada intermediária de auditoria e rastreabilidade
- Os CSVs gerados são posteriormente utilizados na carga para o banco de dados.

repositorio/
- Diretório onde ficam armazenados os arquivos CSV padronizados.
- Representa a área de staging do ETL
- Os arquivos presentes neste diretório são os que efetivamente serão inseridos no banco de dados.

processamento/
- Camada responsável pela inserção dos dados no banco de dados.
- Lê os arquivos CSV do repositório
- Cria a fila de inserção
- Direciona os dados para as tabelas corretas, com base no nome do arquivo
- Representa a etapa Load do ETL.

database/
- Responsável por centralizar as informações relacionadas ao banco de dados.
- Scripts de conexão
- Configurações de acesso (host, usuário, senha, database)
- Funções auxiliares para comunicação com o PostgreSQL

variaveis_globais/
- Contém variáveis utilizadas em todo o escopo do projeto.
- Constantes
- Parâmetros globais
- Configurações reutilizadas em múltiplos módulos

index.py
Arquivo principal responsável por orquestrar a execução do ETL, conectando todas as etapas:
-Inicialização
- Transformação
- Persistência
- Carga no banco

Banco de Dados:
	Tabelas: projeto_kurier_leads, projeto_kurier_clientes, projeto_kurier_vendas
Os scripts de criação das tabelas e inserções encontram-se no diretório scripts_db.

Fluxo do ETL:
-Inicialização da API Local
- Requisição dos dados via API
- Recuperação dos arquivos:
	leads.json
	clientes.json
	vendas.json
- Transformação dos arquivos JSON em CSV (auditoria de dados)
- Leitura dos CSVs padronizados
- Criação de fila de inserção
- Inserção dos dados no banco PostgreSQL

Principais Decisões Técnicas:
- Uso de API Local: simula um cenário real de integração entre sistemas.
- Conversão JSON → CSV: cria uma camada intermediária para auditoria, rastreabilidade e validação futura dos dados.
- Fila de inserção: garante controle do fluxo de carga e organização da inserção por tipo de dado.
- PostgreSQL: banco relacional escolhido pela confiabilidade, compatibilidade com BI e facilidade de integração.
- Roteamento por nome do arquivo: o nome do CSV define automaticamente a tabela de destino, simplificando o processo de carga.

Regras de Negócio Aplicadas:
- Cada arquivo representa uma entidade distinta:
	Leads
	Clientes
	Vendas
- Os dados são padronizados antes da carga:
	Estrutura de colunas consistente
	Tipos de dados compatíveis com o banco
- O nome do arquivo define a tabela de destino no banco de dados.
- A conversão para CSV garante uma camada de auditoria caso seja necessário validar ou reprocessar os dados.

Banco de Dados:
- Banco: PostgreSQL
- Database: definida como parâmetro na função connect_postgres()
- Scripts SQL:
	Criação das tabelas
	Scripts de inserção
    Localizados no diretório: scripts_db

Execução do Projeto
- Clonar este repositório
- Clonar e iniciar o projeto da API Local
- Executar o arquivo .bat para subir a API
- Garantir que o banco PostgreSQL esteja ativo
- Executar o script principal do ETL

Resultado Final:
Ao final do processo, os dados estarão:
- Tratados e padronizados
- Armazenados em PostgreSQL
- Prontos para análise e visualização em ferramentas de BI, como o Power BI