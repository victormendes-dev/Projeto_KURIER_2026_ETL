# Imports do projeto:
import time
from loguru import logger

# Imports locais:
from database.conn_POSTGRES.conn_postgres     import Connect_PgAdmin
from inicializacao.extrair_dados              import retornarDados
from guardar_dados.salvar_dados               import Salvar_Dados
from models.tratar_dados                      import Tratamento
from processamento.Processamento_dados        import Processamento



# Inicio Projeto:
try:
    logger.info("Iniciando execução do projeto")
    # gravando hora do inicio da execução do projeto:
    var_timestampInicio = time.time()

    # Conexão com o postsgres:
    var_objConexao = Connect_PgAdmin()

    # Retorno de dados da API:
    var_jsonDadosKurier = retornarDados()

    try:
        # Organizado dessa forma tendo em vista a ideia de filas. O arquivo já é retornado e é preparado para ser tratado e inserido.
        for nomeArquivo, json in var_jsonDadosKurier.items():

            # Iniciar a classe responsavel por guardar o arquivo no repositorio:
            var_objSalvarDados = Salvar_Dados(json, nomeArquivo)

            # Função responsavel por salvar o arquivo no repositorio:
            var_dfDadosETL = var_objSalvarDados.dados_Excel()

            # Instanciando a classe relacionada ao Tratamento dos dados:
            var_objTratamento = Tratamento(var_dfDadosETL, nomeArquivo)

            # Tratamento dos dados:
            var_dbDados = var_objTratamento.tratamento_de_dados()

            try:
                # Iniciando conexão com o cursor do banco:
                var_objConexaoBanco = var_objConexao.connect_postgres('projeto_Kurier')
                var_objConexaoCursor = var_objConexaoBanco.cursor()

                # Inserção dos dados:
                try: 
                    var_objProcessarDados = Processamento(var_objConexaoBanco,var_objConexaoCursor, var_dbDados, nomeArquivo)
                    var_objProcessarDados.Inserir_dados()
                    
                except var_objConexaoBanco.DatabaseError.pgerror as e:
                    logger.info(f"Erro ao inserir os dados. {e}")
                    var_objConexaoBanco.rollback()
   
            except Exception as e:
                logger.info(f"Erro ao iniciar conexão com o banco. {e}")

    except Exception as e:
        logger.info(f"Ocorreu um erro durante o tratamento dos dados.{e}")

except Exception as e:
    logger.critical(f"Exceção global. {e}")