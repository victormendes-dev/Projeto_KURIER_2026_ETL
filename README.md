ETL API Local – Projeto de Demonstração

Este projeto consiste em um ETL (Extract, Transform, Load) desenvolvido em Python para recuperar e processar dados de uma API local criada para fins avaliativos. 
O pipeline extrai dados de três arquivos JSON, aplica transformações necessárias e os disponibiliza para análise ou armazenamento posterior.

Através do uso do projeto relacionado a API que está no link: 
https://github.com/victormendes-dev/Projeto_KURIER_2026_API

iniciar o arquivo .bat, para iniciar a API e assim deixar a API Local aberta para a recuperação, tratamento e inserção em banco dos arquivos já padronizados para serem
utilizados em uma plataforma de BI, como por exemplo, o PowerBI.

Esse projeto se baseia na recuperação de 3 arquivos, que foram fornecidos para o desafio técnico voltado a vaga de desenvolvedor - pleno.
Ao fazer um request para a API Local, recupera esses 3 arquivos (leads.json, clientes.json e vendas.json)

transforma esses mesmos arquivos JSON em CSV´s para a auditoria de dados posterior ( caso venha a acontecer).
após a transformação e padronização em um CSV, recupera esses mesmos arquivos CSV e cria uma fila para inserção dos dados em banco, tendo como filtro para a inserção 
nas tabelas ( projeto_kurier_clientes, projeto_kurier_leads, projeto_kurier_vendas), o proprio nome dos arquivos, como já está esclarecido dentro do código fonte.

o banco de dados utilizado foi o banco relacional: PostgresSQL e o nome da database que utilizei, está também, nomeada como paramêtro da função "connect_postgres()"

os scripts de criação das tabelas relacionadas ao projeto, está no arquivo scripts_db, assim como os inserts.