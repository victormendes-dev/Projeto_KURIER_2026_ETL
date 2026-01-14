from database.scripts_db import INSERT_TABLE_CLIENTES, INSERT_TABLE_LEADS, INSERT_TABLE_VENDAS
from loguru              import logger

class Processamento:
    def __init__(self, var_objConexaoBanco, var_objConexaoCursor, var_dbDados, nomeArquivo):
        self.var_objConexaoBanco  = var_objConexaoBanco
        self.var_objConexaoCursor = var_objConexaoCursor
        self.var_dbDados          = var_dbDados
        self.nomeArquivo          = nomeArquivo
    
    def Inserir_dados(self):
        try:
            # Processando os dados e inserindo em banco:
            if self.nomeArquivo == "Leads":
                self.var_objConexaoCursor.executemany(INSERT_TABLE_LEADS, self.var_dbDados)
                self.var_objConexaoBanco.commit()
            elif self.nomeArquivo == "Clientes":
                self.var_objConexaoCursor.executemany(INSERT_TABLE_CLIENTES, self.var_dbDados)
                self.var_objConexaoBanco.commit()
            elif self.nomeArquivo == "Vendas":
                self.var_objConexaoCursor.executemany(INSERT_TABLE_VENDAS, self.var_dbDados)
                self.var_objConexaoBanco.commit()

        except:
            raise Exception

        logger.success("Todos os dados foram inseridos com sucesso no banco!")